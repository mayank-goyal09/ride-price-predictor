import streamlit as st
import pandas as pd
import joblib

# ------------------ PAGE CONFIG ------------------ #
st.set_page_config(
    page_title="Ride Price Comparator",
    page_icon="🚕",
    layout="wide",
)

# ------------------ CUSTOM THEME (YELLOW + GREY) ------------------ #
st.markdown(
    """
<style>
.stApp {
    background: radial-gradient(circle at top, #FFD54F 0%, #212121 45%, #121212 100%);
    color: #F5F5F5;
}

/* Make main content sit inside a centered container */
.main > div {
    padding-top: 0.5rem;
}

/* Funky glass card */
.glass-card {
    background: rgba(18, 18, 18, 0.88);
    border-radius: 18px;
    padding: 1.6rem 1.8rem;
    border: 1px solid rgba(255, 235, 59, 0.35);
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.65);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1F1F1F 0%, #101010 100%);
    border-right: 1px solid rgba(255, 235, 59, 0.25);
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #FFEB3B, #FFC107);
    color: #212121 !important;
    border-radius: 999px;
    border: none;
    font-weight: 700;
    padding: 0.5rem 1.4rem;
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.5);
    transition: all 0.18s ease-in-out;
}

.stButton > button:hover {
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.7);
}

/* Inputs */
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stSelectbox > div > div > select,
.stSlider > div > div > div {
    background: rgba(255, 255, 255, 0.06);
    border-radius: 12px;
}

/* Metrics wrapper */
[data-testid="stMetric"] {
    background: rgba(33, 33, 33, 0.95);
    border-radius: 14px;
    padding: 0.8rem 1rem;
    border: 1px solid rgba(255, 235, 59, 0.45);
}

/* Dataframe */
[data-testid="stDataFrame"] {
    background: rgba(18, 18, 18, 0.92);
    border-radius: 14px;
}

/* Section labels */
.section-title {
    font-weight: 800;
    color: #FFEB3B;
    letter-spacing: 0.03em;
    text-transform: uppercase;
    font-size: 0.9rem;
}
</style>
    """,
    unsafe_allow_html=True,
)

# ------------------ TITLE & INTRO ------------------ #
hero_left, hero_right = st.columns([2, 1])

with hero_left:
    st.title("🚕 Ride Price Predictor & Battle Arena")
    st.markdown(
        """
Welcome to the **Uber vs Lyft price fight club**.  
Drop in your ride details, pick your warriors (companies), and this app will:

- 🔮 Predict the estimated price for each company  
- 🥊 Tell you who's being nicer to your wallet (Uber cheaper? Lyft cheaper?)  
        """
    )

with hero_right:
    st.markdown(
        """
<div class='glass-card'>
    <p><strong>Tip:</strong></p>
    <p>Use this like a <strong>smart price radar</strong> before you actually book.<br>
    Play with distance, surge and time to see how <em>dramatically</em> prices react.</p>
</div>
        """,
        unsafe_allow_html=True,
    )

# ------------------ LOAD MODEL ------------------ #
bundle = joblib.load("ride_price_model.pkl")
model = bundle["model"]
model_columns = bundle["columns"]
categorical_cols = bundle["categorical_cols"]

# ------------------ SIDEBAR: COMPANIES ------------------ #
st.sidebar.header("🧃 Company Select")
st.sidebar.write("Pick your fighters for the fare showdown:")

companies = st.sidebar.multiselect(
    "Who's in the ring?",
    ["Uber", "Lyft"],
    default=["Uber", "Lyft"],
)

st.sidebar.markdown("---")
st.sidebar.caption("Pro tip: Select both to unlock **price comparison mode**.")

# ------------------ MAIN INPUT LAYOUT ------------------ #
st.markdown("### 🎛️ Ride configuration")

left_col, right_col = st.columns([1.3, 1])

with left_col:
    st.markdown("<p class='section-title'>Core ride details</p>", unsafe_allow_html=True)

    distance = st.slider("Distance (miles)", 0.5, 20.0, 3.0, 0.1)
    surge = st.slider("Surge multiplier", 1.0, 3.0, 1.0, 0.1)
    hour = st.slider("Hour of day (24h)", 0, 23, 18)

    day_name_to_num = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6,
    }
    day_name = st.selectbox("Day of week", list(day_name_to_num.keys()))
    dayofweek = day_name_to_num[day_name]

with right_col:
    st.markdown("<p class='section-title'>Route & vibe</p>", unsafe_allow_html=True)

    all_uber_cats = ["UberX", "UberPool", "UberXL"]
    all_lyft_cats = ["Lyft", "Lyft Shared", "Lyft XL"]

    if companies == ["Uber"]:
        ride_options = all_uber_cats
    elif companies == ["Lyft"]:
        ride_options = all_lyft_cats
    else:
        ride_options = all_uber_cats + all_lyft_cats

    ride_category = st.selectbox("Ride category", ride_options)

    source = st.text_input("Pickup area", "Back Bay")
    destination = st.text_input("Dropoff area", "North End")
    st.caption("Make these realistic — models love clean geography. 😉")

# ------------------ FEATURE BUILDING ------------------ #
def build_features(cab_type, name):
    data = {
        "distance": [distance],
        "surge_multiplier": [surge],
        "hour": [hour],
        "dayofweek": [dayofweek],
        "cab_type": [cab_type],
        "name": [name],
        "source": [source],
        "destination": [destination],
    }
    df = pd.DataFrame(data)
    df_enc = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    df_enc = df_enc.reindex(columns=model_columns, fill_value=0)
    return df_enc


def map_ride_category(company):
    if company == "Uber":
        return ride_category if ride_category in all_uber_cats else "UberX"
    elif company == "Lyft":
        return ride_category if ride_category in all_lyft_cats else "Lyft"
    return ride_category

# ------------------ PREDICTION ACTION + TABS ------------------ #
st.markdown("### 🧮 Prediction Zone")

tabs = st.tabs(["😌 Simple Mode", "🧠 Nerd Mode"])

with tabs[0]:
    st.markdown("#### 😌 Simple Mode · Just tell me the prices")

    go_simple = st.button("Predict price 💰", use_container_width=True, key="simple_go")

    if go_simple:
        if not companies:
            st.warning("Select **at least one** company on the left sidebar to start the battle.")
        else:
            results = {}
            for c in companies:
                name_for_c = map_ride_category(c)
                X_feat = build_features(cab_type=c, name=name_for_c)
                price = float(model.predict(X_feat)[0])
                results[c] = price

            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.subheader("📊 Estimated prices (USD)")

            metric_cols = st.columns(len(results))
            for col, (c, price) in zip(metric_cols, results.items()):
                trend = [price * (0.97 + i * 0.01) for i in range(5)]
                with col:
                    st.metric(
                        label=f"{c} · {map_ride_category(c)}",
                        value=f"${price:0.2f}",
                        delta=None,
                    )

            if "Uber" in results and "Lyft" in results:
                diff = results["Uber"] - results["Lyft"]

                st.markdown("---")
                if diff > 0:
                    st.error(
                        f"🚨 **Wallet alert!** Uber looks "
                        f"`${abs(diff):0.2f}` more expensive than Lyft for this setup."
                    )
                    st.caption("Maybe Lyft is in a good mood today. 🕺")
                elif diff < 0:
                    st.success(
                        f"🤑 **Nice!** Uber seems `${abs(diff):0.2f}` cheaper than Lyft "
                        "for this exact ride."
                    )
                    st.caption("Surge, time and route can flip this. Try tweaking the sliders.")
                else:
                    st.info("🤝 It's a tie! Uber and Lyft look roughly the same for this ride.")
                    st.caption("Try changing distance or hour to break the tie.")
            else:
                st.info("Add both Uber and Lyft in the sidebar to unlock the comparison mode.")

            st.markdown("</div>", unsafe_allow_html=True)

with tabs[1]:
    st.markdown("#### 🧠 Nerd Mode · Show me the guts")

    go_nerd = st.button(
        "Run prediction with full feature view 🔎",
        use_container_width=True,
        key="nerd_go",
    )

    if go_nerd:
        if not companies:
            st.warning("Select at least one company first.")
        else:
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.subheader("🔬 Model input rows")

            results = {}
            for c in companies:
                name_for_c = map_ride_category(c)
                X_feat = build_features(cab_type=c, name=name_for_c)
                price = float(model.predict(X_feat)[0])
                results[c] = {"price": price, "features": X_feat}

            for c, content in results.items():
                st.markdown(f"##### {c} · {map_ride_category(c)}")
                st.write(f"**Predicted price:** `${content['price']:0.2f}`")
                st.dataframe(content["features"], use_container_width=True)
                st.markdown("---")

            st.markdown("</div>", unsafe_allow_html=True)

# ------------------ FUN FOOTER ------------------ #
st.markdown(
    """
<hr style="border-color: rgba(255,255,255,0.2); margin-top: 2rem;"/>
<div style="text-align: center; color: #F5F5F5; font-size: 0.9rem; padding-bottom: 0.7rem;">
    built by <b>Mayank's ML brain 🧠</b> · powered by Streamlit &amp; scikit-learn
</div>
    """,
    unsafe_allow_html=True,
)
