"""
Insubordinate & Churlish - VC Flow
A dashboard visualizing how venture capital shifted across sectors, 2022-2025.

Run locally:
    source venv/bin/activate
    streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "vc_by_sector.csv"

st.set_page_config(
    page_title="VC Flow 2022-2025",
    page_icon=":moneybag:",
    layout="wide",
)

st.title("VC Flow: How Venture Capital Shifted by Sector, 2022-2025")
st.caption("Primary source: CB Insights State of Venture | Supplements: PitchBook-NVCA, Crunchbase")

# ── Load data ───────────────────────────────────────────────────────────

@st.cache_data
def load_data():
    if not DATA_PATH.exists():
        return None
    return pd.read_csv(DATA_PATH)

df = load_data()

if df is None:
    st.warning(
        f"No data file yet at `{DATA_PATH.relative_to(Path(__file__).parent)}`. "
        "Drop a CSV here with columns: `year`, `quarter`, `sector`, `deal_value_usd_b`, `deal_count`, `source`."
    )
    st.stop()

# ── Sidebar filters ─────────────────────────────────────────────────────

st.sidebar.header("Filters")
years = sorted(df["year"].unique())
year_range = st.sidebar.select_slider(
    "Year range", options=years, value=(years[0], years[-1])
)
sectors = sorted(df["sector"].unique())
chosen_sectors = st.sidebar.multiselect(
    "Sectors", options=sectors, default=sectors
)

mask = (
    df["year"].between(year_range[0], year_range[1])
    & df["sector"].isin(chosen_sectors)
)
view = df[mask]

# ── Feature 1: total deal value over time, by sector ─────────────────────

st.subheader("Deal value over time, by sector")
ts = view.groupby(["year", "quarter", "sector"], as_index=False)["deal_value_usd_b"].sum()
ts["period"] = ts["year"].astype(str) + " Q" + ts["quarter"].astype(str)
fig = px.line(
    ts, x="period", y="deal_value_usd_b", color="sector",
    markers=True,
    labels={"deal_value_usd_b": "Deal value ($B)", "period": "Quarter"},
)
st.plotly_chart(fig, use_container_width=True)

# ── Feature 2: sector share over time (stacked area) ─────────────────────

st.subheader("Sector share of total VC")
share = view.groupby(["year", "quarter", "sector"], as_index=False)["deal_value_usd_b"].sum()
share["period"] = share["year"].astype(str) + " Q" + share["quarter"].astype(str)
totals = share.groupby("period")["deal_value_usd_b"].transform("sum")
share["share_pct"] = (share["deal_value_usd_b"] / totals) * 100
fig2 = px.area(
    share, x="period", y="share_pct", color="sector",
    labels={"share_pct": "Share of total (%)", "period": "Quarter"},
)
st.plotly_chart(fig2, use_container_width=True)

# ── Feature 3: top movers (biggest gainers / losers) ─────────────────────

st.subheader("Top sector movers: change in deal value, first year vs last year")
first_year, last_year = year_range
yr_totals = view.groupby(["year", "sector"], as_index=False)["deal_value_usd_b"].sum()
pivot = yr_totals.pivot(index="sector", columns="year", values="deal_value_usd_b").fillna(0)
if first_year in pivot.columns and last_year in pivot.columns:
    pivot["delta"] = pivot[last_year] - pivot[first_year]
    pivot = pivot.sort_values("delta", ascending=False)
    fig3 = px.bar(
        pivot.reset_index(),
        x="sector", y="delta",
        color="delta", color_continuous_scale="RdYlGn",
        labels={"delta": f"$B change ({first_year} → {last_year})"},
    )
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.info("Need data for both endpoint years to compute movers.")

# ── Feature 4: data table with sources ──────────────────────────────────

st.subheader("Underlying data (with sources)")
st.dataframe(view, use_container_width=True)
st.caption(
    "Each row should cite a source. See `sources.md` for the full list of references. "
    "If you see a number without a source, treat it as a placeholder."
)
