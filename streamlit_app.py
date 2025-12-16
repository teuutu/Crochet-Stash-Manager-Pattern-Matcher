# streamlit_app.py
import streamlit as st
import pandas as pd
import json
from db_manager import get_inventory, get_patterns, add_sample_data, init_db
from crochet_analyzer import find_matching_patterns


init_db()
add_sample_data()


def load_data():
    """Loads data from the database and prepares it for display."""
    inventory = get_inventory()
    patterns_raw = get_patterns()


    patterns_display = []
    for p in patterns_raw:

        try:

            p['instructions'] = json.loads(p['instructions'].replace("'", '"'))
        except:
            pass


        p['Steps Preview'] = ' | '.join(p['instructions'][:3]) + '...' if isinstance(p['instructions'], list) else p[
                                                                                                                       'instructions'][
                                                                                                                       :50] + '...'
        patterns_display.append(p)

    return pd.DataFrame(inventory), pd.DataFrame(patterns_display)




st.set_page_config(
    page_title="Intelligent Crochet Pattern Utility",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧶 Intelligent Crochet Pattern Utility")
st.markdown("### Real-Time Inventory Analysis and Project Recommendations")
#


inventory_df, patterns_df = load_data()


tab_inventory, tab_library, tab_analysis = st.tabs(["🏡 Yarn Stash", "📚 Pattern Library", "✨ Project Analysis"])

with tab_inventory:
    st.header("Current Yarn Inventory")
    if not inventory_df.empty:

        inventory_df_display = inventory_df[['name', 'weight', 'hook_size_mm', 'yardage', 'quantity']]
        st.dataframe(inventory_df_display, use_container_width=True)
    else:
        st.info("The inventory is empty.")

    st.markdown("---")
    st.caption(
        "*Note: You can manually add more records to the `yarn_inventory` table in the `crochet_inventory.db` file.*")

with tab_library:
    st.header("Pattern Library")
    if not patterns_df.empty:

        patterns_df_display = patterns_df[['name', 'required_weight', 'complexity', 'Steps Preview']]
        st.dataframe(patterns_df_display, use_container_width=True)
    else:
        st.info("The pattern library is empty.")

    st.markdown("---")
    st.caption("*The 'Steps Preview' column demonstrates simple text analysis (NLP) of the instructions.*")

with tab_analysis:
    st.header("Project Recommendations")


    if st.button("🔎 Run Project Analysis"):
        st.subheader("Results:")


        inventory_list = inventory_df.to_dict('records')
        patterns_list = patterns_df.to_dict('records')


        results = find_matching_patterns(inventory_list, patterns_list)

        if results:
            st.success(f"🎉 Success! Found **{len(results)}** potential projects you can start NOW!")


            results_df = pd.DataFrame(results)
            st.dataframe(results_df, use_container_width=True)

            st.markdown("---")
            st.warning(
                "⚠️ **Stitch Estimate** is the result of the simple text processing function in `crochet_data.py` (basic NLP).")

        else:
            st.error("No matches found. Check your stash requirements or add new patterns!")