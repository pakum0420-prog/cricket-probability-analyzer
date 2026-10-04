import streamlit as st
import matplotlib.pyplot as plt

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Cricket Probability Analyzer",
    page_icon="🏏",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Main title */

.hero {
    background: linear-gradient(135deg, #071952, #0B666A);
    padding: 35px;
    border-radius: 22px;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.12);
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 8px;
}

.hero p {
    font-size: 18px;
    opacity: 0.9;
}

/* Section headings */

.section-title {
    font-size: 25px;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 15px;
}

/* Cards */

.metric-card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    border: 1px solid #eeeeee;
}

.metric-title {
    color: #666;
    font-size: 15px;
}

.metric-value {
    font-size: 30px;
    font-weight: 700;
    margin-top: 5px;
}

/* Analyze button */

.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: 700;
}

/* Input box */

div[data-baseweb="input"] {
    border-radius: 10px;
}

/* Footer */

.footer {
    text-align: center;
    color: #777;
    margin-top: 40px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero">

<h1>🏏 Cricket Probability Analyzer</h1>

<p>
Analyze runs, wickets, boundaries and scoring patterns
using probability and statistical analysis.
</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# INPUT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">📝 Enter Match Data</div>',
    unsafe_allow_html=True
)

st.info(
    "Enter the number of balls and the outcomes recorded in those balls."
)

col1, col2, col3 = st.columns(3)

with col1:

    total_balls = st.number_input(
        "🏏 Total Balls",
        min_value=1,
        value=100,
        step=1
    )

    dot_balls = st.number_input(
        "⚫ Dot Balls",
        min_value=0,
        value=40,
        step=1
    )

    one_runs = st.number_input(
        "1️⃣ One Run",
        min_value=0,
        value=25,
        step=1
    )

with col2:

    two_runs = st.number_input(
        "2️⃣ Two Runs",
        min_value=0,
        value=15,
        step=1
    )

    three_runs = st.number_input(
        "3️⃣ Three Runs",
        min_value=0,
        value=5,
        step=1
    )

    fours = st.number_input(
        "4️⃣ Fours",
        min_value=0,
        value=10,
        step=1
    )

with col3:

    sixes = st.number_input(
        "6️⃣ Sixes",
        min_value=0,
        value=5,
        step=1
    )

    wickets = st.number_input(
        "🔴 Wickets",
        min_value=0,
        value=2,
        step=1
    )

# =========================================================
# ANALYZE BUTTON
# =========================================================

st.write("")

analyze = st.button(
    "🔍 ANALYZE MATCH",
    type="primary"
)

# =========================================================
# ANALYSIS
# =========================================================

if analyze:

    # ---------------------------------------------
    # Validate data
    # ---------------------------------------------

    total_recorded = (
        dot_balls
        + one_runs
        + two_runs
        + three_runs
        + fours
        + sixes
    )

    if total_recorded != total_balls:

        st.error(
            f"""
            ⚠️ The ball outcomes add up to **{total_recorded} balls**,
            but Total Balls is **{total_balls}**.

            Please make sure the event counts add up to the total number
            of balls.
            """
        )

        st.stop()

    # ---------------------------------------------
    # Probabilities
    # ---------------------------------------------

    p_dot = dot_balls / total_balls
    p_one = one_runs / total_balls
    p_two = two_runs / total_balls
    p_three = three_runs / total_balls
    p_four = fours / total_balls
    p_six = sixes / total_balls
    p_wicket = wickets / total_balls

    # ---------------------------------------------
    # Boundary calculation
    # ---------------------------------------------

    total_boundaries = fours + sixes

    p_boundary = total_boundaries / total_balls

    # ---------------------------------------------
    # Total runs
    # ---------------------------------------------

    total_runs = (
        (one_runs * 1)
        + (two_runs * 2)
        + (three_runs * 3)
        + (fours * 4)
        + (sixes * 6)
    )

    # ---------------------------------------------
    # Average runs
    # ---------------------------------------------

    average_runs = total_runs / total_balls

    # =================================================
    # SUCCESS MESSAGE
    # =================================================

    st.success("✅ Match analyzed successfully!")

    # =================================================
    # KEY STATISTICS
    # =================================================

    st.markdown(
        '<div class="section-title">📊 Match Statistics</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">TOTAL RUNS</div>
                <div class="metric-value">{total_runs}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">RUNS / BALL</div>
                <div class="metric-value">{average_runs:.2f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">BOUNDARIES</div>
                <div class="metric-value">{total_boundaries}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">WICKETS</div>
                <div class="metric-value">{wickets}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # =================================================
    # PROBABILITY TABLE
    # =================================================

    st.markdown(
        '<div class="section-title">🎯 Event Probabilities</div>',
        unsafe_allow_html=True
    )

    probability_data = {
        "Event": [
            "Dot Ball",
            "1 Run",
            "2 Runs",
            "3 Runs",
            "Four",
            "Six",
            "Wicket"
        ],

        "Occurrences": [
            dot_balls,
            one_runs,
            two_runs,
            three_runs,
            fours,
            sixes,
            wickets
        ],

        "Probability": [
            f"{p_dot * 100:.2f}%",
            f"{p_one * 100:.2f}%",
            f"{p_two * 100:.2f}%",
            f"{p_three * 100:.2f}%",
            f"{p_four * 100:.2f}%",
            f"{p_six * 100:.2f}%",
            f"{p_wicket * 100:.2f}%"
        ]
    }

    st.dataframe(
        probability_data,
        use_container_width=True,
        hide_index=True
    )

    # =================================================
    # SPECIAL PROBABILITIES
    # =================================================

    st.markdown(
        '<div class="section-title">🔥 Key Probabilities</div>',
        unsafe_allow_html=True
    )

    p1, p2, p3 = st.columns(3)

    with p1:

        st.metric(
            "💥 Boundary Probability",
            f"{p_boundary * 100:.2f}%"
        )

    with p2:

        st.metric(
            "🎯 Wicket Probability",
            f"{p_wicket * 100:.2f}%"
        )

    with p3:

        st.metric(
            "🏏 Average Runs / Ball",
            f"{average_runs:.2f}"
        )

    # =================================================
    # CHARTS
    # =================================================

    st.markdown(
        '<div class="section-title">📈 Visual Analysis</div>',
        unsafe_allow_html=True
    )

    chart_col1, chart_col2 = st.columns(2)

    # ---------------------------------------------
    # Probability Chart
    # ---------------------------------------------

    events = [
        "Dot",
        "1 Run",
        "2 Runs",
        "3 Runs",
        "Four",
        "Six"
    ]

    probabilities = [
        p_dot * 100,
        p_one * 100,
        p_two * 100,
        p_three * 100,
        p_four * 100,
        p_six * 100
    ]

    with chart_col1:

        fig, ax = plt.subplots(figsize=(7, 5))

        ax.bar(
            events,
            probabilities
        )

        ax.set_title(
            "Probability of Cricket Events"
        )

        ax.set_ylabel(
            "Probability (%)"
        )

        ax.set_xlabel(
            "Event"
        )

        plt.xticks(rotation=30)

        st.pyplot(fig)

    # ---------------------------------------------
    # Boundary Chart
    # ---------------------------------------------

    with chart_col2:

        boundary_names = [
            "Fours",
            "Sixes"
        ]

        boundary_values = [
            fours,
            sixes
        ]

        fig2, ax2 = plt.subplots(figsize=(7, 5))

        ax2.bar(
            boundary_names,
            boundary_values
        )

        ax2.set_title(
            "Fours vs Sixes"
        )

        ax2.set_ylabel(
            "Occurrences"
        )

        ax2.set_xlabel(
            "Boundary Type"
        )

        st.pyplot(fig2)

    # =================================================
    # FINAL SUMMARY
    # =================================================

    st.markdown(
        '<div class="section-title">📋 Analysis Summary</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        **Total Balls:** {total_balls}

        **Total Runs:** {total_runs}

        **Average Runs per Ball:** {average_runs:.2f}

        **Total Boundaries:** {total_boundaries}

        **Boundary Probability:** {p_boundary * 100:.2f}%

        **Wicket Probability:** {p_wicket * 100:.2f}%
        """
    )

    st.success(
        "🏆 Probability analysis completed successfully!"
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        🏏 Cricket Probability Analyzer
        <br>
        Probability • Statistics • Data Visualization
    </div>
    """,
    unsafe_allow_html=True
)