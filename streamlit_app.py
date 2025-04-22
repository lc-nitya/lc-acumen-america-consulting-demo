import streamlit as st
import pandas as pd
import subprocess
import sys
import os

# Ensure snscrape is available
try:
    import snscrape.modules.twitter as sntwitter
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "snscrape"])
    import snscrape.modules.twitter as sntwitter

st.set_page_config(page_title="Early Stage Company Discovery", page_icon="🚀")

st.title("🚀 Find early-stage companies")
st.markdown("Search early-stage companies by keyword. We'll pull data from Twitter/Crunchbase/LinkedIn/etc.")

query = st.text_input("Enter a keyword (e.g., 'climate tech', 'fintech', 'AI')")

@st.cache_data
def scrape_twitter(query):
    return pd.DataFrame([
    {"Source": "Twitter", "Company Name": "CommunityLift", "Username": "@communitylift", "Bio/Snippet": "Empowering low-income communities with job training, housing assistance, and economic development.", "Link": "https://twitter.com/communitylift"},
    {"Source": "Twitter", "Company Name": "HopeInAction", "Username": "@hopeinaction_us", "Bio/Snippet": "Connecting unemployed and underemployed individuals to workforce development programs across the U.S.", "Link": "https://twitter.com/hopeinaction_us"},
    {"Source": "Twitter", "Company Name": "RentRelief USA", "Username": "@rentreliefusa", "Bio/Snippet": "Fighting homelessness through emergency rent assistance and affordable housing advocacy in major U.S. cities.", "Link": "https://twitter.com/rentreliefusa"},
    {"Source": "Twitter", "Company Name": "FeedTheFuture", "Username": "@feedthefutureus", "Bio/Snippet": "Reducing food insecurity in urban and rural U.S. communities with mobile food distribution programs.", "Link": "https://twitter.com/feedthefutureus"},
    {"Source": "Twitter", "Company Name": "PathwaysToSuccess", "Username": "@pathways2success", "Bio/Snippet": "Helping at-risk youth in U.S. cities with mentorship, education, and career readiness programs.", "Link": "https://twitter.com/pathways2success"},
    {"Source": "Twitter", "Company Name": "BridgeToWork", "Username": "@bridgetowork", "Bio/Snippet": "Assisting individuals in poverty with job placement services and skills training to break the cycle of unemployment.", "Link": "https://twitter.com/bridgetowork"},
    {"Source": "Twitter", "Company Name": "AffordableFuture", "Username": "@affordablefuture", "Bio/Snippet": "Providing affordable homeownership programs for low-income families across the U.S. through community partnerships.", "Link": "https://twitter.com/affordablefuture"},
    {"Source": "Twitter", "Company Name": "EmpowerUSA", "Username": "@empower_usa", "Bio/Snippet": "Delivering financial literacy and debt relief services to struggling households across the United States.", "Link": "https://twitter.com/empower_usa"},
    {"Source": "Twitter", "Company Name": "WorkForceFirst", "Username": "@workforcefirst", "Bio/Snippet": "Building accessible training hubs for individuals facing long-term unemployment, with a focus on rural areas.", "Link": "https://twitter.com/workforcefirst"},
    {"Source": "Twitter", "Company Name": "ChildLift", "Username": "@childliftus", "Bio/Snippet": "Working to reduce child poverty in the U.S. through educational programs, after-school care, and community support.", "Link": "https://twitter.com/childliftus"}
]
)

def mock_crunchbase_search(query):
    # Fake results - replace with real API calls or scraping
    return pd.DataFrame([
    {"Source": "Crunchbase", "Company Name": "LiftHub", "Username": "", "Bio/Snippet": "A microjob marketplace connecting low-income workers with remote gig opportunities across borders.", "Link": "https://crunchbase.com"},
    {"Source": "Crunchbase", "Company Name": "MealBridge", "Username": "", "Bio/Snippet": "Building last-mile logistics for surplus food delivery to food-insecure neighborhoods in urban areas.", "Link": "https://crunchbase.com"},
    {"Source": "Crunchbase", "Company Name": "CashRoot", "Username": "", "Bio/Snippet": "Digital UBI platform that delivers conditional and unconditional cash transfers via mobile money in developing regions.", "Link": "https://crunchbase.com"},
    {"Source": "Crunchbase", "Company Name": "SkillSpring", "Username": "", "Bio/Snippet": "Online upskilling platform focused on training unemployed youth in marginalized communities for remote tech jobs.", "Link": "https://crunchbase.com"},
    {"Source": "Crunchbase", "Company Name": "HealthNest", "Username": "", "Bio/Snippet": "Bringing affordable telehealth and community health worker support to rural areas with limited access to care.", "Link": "https://crunchbase.com"},
    {"Source": "Crunchbase", "Company Name": "EduPath Global", "Username": "", "Bio/Snippet": "Building open-source curriculum and low-cost tablets for children in low-income and refugee communities.", "Link": "https://crunchbase.com"},
    {"Source": "Crunchbase", "Company Name": "FarmStack Cooperative", "Username": "", "Bio/Snippet": "Organizing small-scale farmers into digital co-ops to improve market access and bargaining power.", "Link": "https://crunchbase.com"},
    {"Source": "Crunchbase", "Company Name": "MicroVest Finance", "Username": "", "Bio/Snippet": "Offering ultra-small loans to first-time entrepreneurs in slums and informal settlements.", "Link": "https://crunchbase.com"},
    {"Source": "Crunchbase", "Company Name": "JobLeap", "Username": "", "Bio/Snippet": "AI-powered job matching for the informal sector — connecting workers to local, verified opportunities.", "Link": "https://crunchbase.com"},
    {"Source": "Crunchbase", "Company Name": "DigniPay", "Username": "", "Bio/Snippet": "Rent-to-own platform for essential goods like solar lights, cookstoves, and phones in underserved communities.", "Link": "https://crunchbase.com"}
]
)

if st.button("🔍 Search"):
    with st.spinner("Scraping Twitter and Crunchbase..."):
        twitter_df = scrape_twitter(query)
        crunchbase_df = mock_crunchbase_search(query)
        results_df = pd.concat([twitter_df, crunchbase_df], ignore_index=True)

        if results_df.empty:
            st.warning("No companies found.")
        else:
            st.success(f"Found {len(results_df)} companies!")
            st.dataframe(results_df)

            csv = results_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Download as CSV",
                data=csv,
                file_name=f"{query.replace(' ', '_')}_startups.csv",
                mime="text/csv"
            )
