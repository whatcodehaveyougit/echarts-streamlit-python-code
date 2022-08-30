import inspect
import textwrap

import streamlit as st

from demo_echarts import ST_DEMOS
from demo_pyecharts import ST_PY_DEMOS

from streamlit_echarts import JsCode
from streamlit_echarts import st_echarts


def main():
    st.title("Streamlit ECharts Demooo")

    option = st.selectbox(
         'How would you like to be contacted?',
         ('Email', 'Home phone', 'Mobile phone'))

    st.write('You selected:', option)

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
    data = [
        [
            [10.0, 8.04],
            [8.0, 6.95],
            [13.0, 7.58],
            [9.0, 8.81],
            [11.0, 8.33],
            [14.0, 9.96],
            [6.0, 7.24],
            [4.0, 4.26],
            [12.0, 10.84],
            [7.0, 4.82],
            [5.0, 5.68],
        ],
        [
            [10.0, 9.14],
            [8.0, 8.14],
            [13.0, 8.74],
            [9.0, 8.77],
            [11.0, 9.26],
            [14.0, 8.10],
            [6.0, 6.13],
            [4.0, 3.10],
            [12.0, 9.13],
            [7.0, 7.26],
            [5.0, 4.74],
        ],
        [
            [10.0, 7.46],
            [8.0, 6.77],
            [13.0, 12.74],
            [9.0, 7.11],
            [11.0, 7.81],
            [14.0, 8.84],
            [6.0, 6.08],
            [4.0, 5.39],
            [12.0, 8.15],
            [7.0, 6.42],
            [5.0, 5.73],
        ],
        [
            [8.0, 6.58],
            [8.0, 5.76],
            [8.0, 7.71],
            [8.0, 8.84],
            [8.0, 8.47],
            [8.0, 7.04],
            [8.0, 5.25],
            [19.0, 12.50],
            [8.0, 5.56],
            [8.0, 7.91],
            [8.0, 6.89],
        ],
    ]

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
            {"gridIndex": 0, "min": 0, "max": 20},
            {"gridIndex": 1, "min": 0, "max": 20},
            {"gridIndex": 2, "min": 0, "max": 20},
            {"gridIndex": 3, "min": 0, "max": 20},
        ],
        "yAxis": [
            {"gridIndex": 0, "min": 0, "max": 15},
            {"gridIndex": 1, "min": 0, "max": 15},
            {"gridIndex": 2, "min": 0, "max": 15},
            {"gridIndex": 3, "min": 0, "max": 15},
        ],
        "series": [
            {
                "name": "I",
                "type": "scatter",
                "xAxisIndex": 0,
                "yAxisIndex": 0,
                "data": data[0],
                "markLine": line_opt,
            },
            {
                "name": "II",
                "type": "scatter",
                "xAxisIndex": 1,
                "yAxisIndex": 1,
                "data": data[1],
                "markLine": line_opt,
            },
            {
                "name": "III",
                "type": "scatter",
                "xAxisIndex": 2,
                "yAxisIndex": 2,
                "data": data[2],
                "markLine": line_opt,
            },
            {
                "name": "IV",
                "type": "scatter",
                "xAxisIndex": 3,
                "yAxisIndex": 3,
                "data": data[3],
                "markLine": line_opt,
            },
        ],
    }
    st_echarts(options=option, height="600px")

render_anscombe_quartet()