import inspect
import textwrap

import streamlit as st

from demo_echarts import ST_DEMOS
from demo_pyecharts import ST_PY_DEMOS

from streamlit_echarts import JsCode
from streamlit_echarts import st_echarts


def main():
    st.title("Streamlit ECharts Demooo")

    # with st.sidebar:
    #     st.header("Configuration")
        # api_options = ("echarts", "pyecharts")
        # selected_api = st.selectbox(
        #     label="Choose your preferred API:",
        #     options=api_options,
        # )

        # page_options = (
        #     list(ST_PY_DEMOS.keys())
        #     if selected_api == "pyecharts"
        #     else list(ST_DEMOS.keys())
        # )
        # selected_page = st.selectbox(
        #     label="Choose an example",
        #     options=page_options,
        # )
        # demo, url = (
        #     ST_DEMOS[selected_page]
        #     if selected_api == "echarts"
        #     else ST_PY_DEMOS[selected_page]
        # )

        # if selected_api == "echarts":
        #     st.caption(
        #         """ECharts demos are extracted from https://echarts.apache.org/examples/en/index.html, 
        #     by copying/formattting the 'option' json object into st_echarts.
        #     Definitely check the echarts example page, convert the JSON specs to Python Dicts and you should get a nice viz."""
        #     )
        # if selected_api == "pyecharts":
        #     st.caption(
        #         """Pyecharts demos are extracted from https://github.com/pyecharts/pyecharts-gallery,
        #     by copying the pyecharts object into st_pyecharts. 
        #     Pyecharts is still using ECharts 4 underneath, which is why the theming between st_echarts and st_pyecharts is different."""
        #     )

#     demo()

#     sourcelines, _ = inspect.getsourcelines(demo)
#     with st.expander("Source Code"):
#         st.code(textwrap.dedent("".join(sourcelines[1:])))
#     st.markdown(f"Credit: {url}")


# if __name__ == "__main__":
#     st.set_page_config(
#         page_title="Streamlit ECharts Demo", page_icon=":chart_with_upwards_trend:"
#     )
#     main()
#     with st.sidebar:
#         st.markdown("---")
#         st.markdown(
#             '<h6>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp by <a href="https://twitter.com/andfanilo">@andfanilo</a></h6>',
#             unsafe_allow_html=True,
#         )
#         st.markdown(
#             '<div style="margin-top: 0.75em;"><a href="https://www.buymeacoffee.com/andfanilo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></div>',
#             unsafe_allow_html=True,
#         )


def render_anscombe_quartet():

    # see_results_from_this_day = st.selectbox(
    #     'Select the first day you want to see results from',
    #     ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'))
    # st.write('You selected:', see_results_from_this_day)
    
    # see_results_until_this_day = st.selectbox(
    #     'Select the last day you want to see results from',
    #     ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'))
    # st.write('You selected:', see_results_until_this_day)

    days_of_week_for_slider = 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'

    see_results_from_this_day, see_results_until_this_day = st.select_slider(
        "Slider Range:",
        options=days_of_week_for_slider,
        value=("Tue", "Sat")
    )

    st.write( "You choose: ", see_results_from_this_day, "to", see_results_until_this_day )



    data = [
        [
            120,
            100,
            150,
            80,
            70,
            40,
            100,
        ],
        [
            160,
            200,
            123,
            80,
            70,
            8,
            130,
        ],
        [
            50,
            150,
            150,
            45,
            40,
            10,
            80,
        ],
        [
            90,
            180,
            150,
            85,
            40,
            10,
            130,
        ],
    ]

    days_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    days_of_the_week_to_show = []
    for day in days_of_the_week:
        if ( ( day != see_results_from_this_day ) and ( len( days_of_the_week_to_show ) == 0 ) ):
            continue
        if len( days_of_the_week_to_show ) == 0: 
            days_of_the_week_to_show.append( day )
            continue
        if day != see_results_until_this_day:
             days_of_the_week_to_show.append( day )
        else:
            days_of_the_week_to_show.append( day )
            break




    line_opt = {
        "animation": False,
        "label": {"formatter": "y = 0.5 * x + 3", "align": "right"},
        "lineStyle": {"type": "solid"},
        "tooltip": {"formatter": "y = 0.5 * x + 3"},
        "data": [
            [{"coord": [0, 3], "symbol": None}, {"coord": [20, 13], "symbol": None}]
        ],
    }

    option = {
        "title": {"text": "Anscombe's quartet", "left": "center", "top": 0},
        "grid": [
            {"left": "7%", "top": "7%", "width": "38%", "height": "38%"},
            {"right": "7%", "top": "7%", "width": "38%", "height": "38%"},
            {"left": "7%", "bottom": "7%", "width": "38%", "height": "38%"},
            {"right": "7%", "bottom": "7%", "width": "38%", "height": "38%"},
        ],
        "tooltip": {"formatter": "Group {a}: ({c})"},
        "xAxis": [
            { "gridIndex": 0, "type": "category", "data": days_of_the_week_to_show },
            { "gridIndex": 1, "type": "category", "data": days_of_the_week_to_show },
            { "gridIndex": 2, "type": "category", "data": days_of_the_week_to_show },
            { "gridIndex": 3, "type": "category", "data": days_of_the_week_to_show }
        ],
        "yAxis": [
            { "gridIndex": 0, "type": "value"},
            { "gridIndex": 1, "type": "value"},
            { "gridIndex": 2, "type": "value"},
            { "gridIndex": 3, "type": "value"}
        ],
        "series": [
              {
                "name": "I",
                "xAxisIndex": 0,
                "yAxisIndex": 0,
                "data": data[0],
                "type": "bar",
            },
           {
                "name": "2",
                "xAxisIndex": 1,
                "yAxisIndex": 1,
                "data": data[1],
                "type": "bar",
            },
            {
                "name": "3",
                "xAxisIndex": 2,
                "yAxisIndex": 2,
                "data": data[2],
                "type": "bar",
            },
            {
                "name": "4",
                "xAxisIndex": 3,
                "yAxisIndex": 3,
                "data": data[3],
                "type": "bar",
            },
        ],
    }
    st_echarts(options=option, height="600px")

render_anscombe_quartet()


# --------------------------- NEW FUNCTION -------------------------------

def render_basic_bar():
    options = {
        "xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type": "value"},
        "series": [{"data": [120, 200, 150, 80, 70, 110, 130], "type": "bar"}],
        "dataZoom": [{
            "type": 'inside',
            "xAxisIndex": 0,
            "filterMode": 'weakFilter',
        }]
    }
    st_echarts(options=options, height="500px")

render_basic_bar()