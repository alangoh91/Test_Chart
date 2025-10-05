from flask import Flask, render_template
from pyecharts.charts import Line, Bar
from pyecharts import options as opts
import random

app = Flask(__name__)


def generate_data():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    margins = [round(random.uniform(5, 25), 2) for _ in range(12)]
    return months, margins


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/chart')
def index():
    months, margins = generate_data()

    # Create Line chart
    line = Line()
    line.add_xaxis(months)
    line.add_yaxis(
        "Net Profit Margin (%)",
        margins,
        is_smooth=True,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=2)
    )

    # Set global options
    line.set_global_opts(
        title_opts=opts.TitleOpts(title="Net Profit Margin Over Time"),
        xaxis_opts=opts.AxisOpts(name="Month"),
        yaxis_opts=opts.AxisOpts(name="Net Profit Margin (%)"),
        tooltip_opts=opts.TooltipOpts(trigger="axis")
    )

    return render_template("line_chart.html", chart=line.render_embed())


@app.route('/bar')
def bar_chart():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    margins = [round(random.uniform(5, 25), 2) for _ in range(12)]

    bar = Bar()
    bar.add_xaxis(months)
    bar.add_yaxis("Net Profit Margin (%)", margins)
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Net Profit Margin Bar Chart"),
        xaxis_opts=opts.AxisOpts(name="Month"),
        yaxis_opts=opts.AxisOpts(name="Net Profit Margin (%)"),
        tooltip_opts=opts.TooltipOpts(trigger="axis")
    )

    return render_template("bar_chart.html", chart=bar.render_embed())


if __name__ == '__main__':
    app.run(debug=True)
