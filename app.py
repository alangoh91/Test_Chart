from flask import Flask, render_template
from pyecharts.charts import Line, Bar
from pyecharts import options as opts
import random
import plotly.graph_objs as go
import plotly.offline as pyo

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


@app.route('/revenue_growth')
def revenue_growth():
    years = [str(y) for y in range(2018, 2024)]
    revenue = [round(random.uniform(100, 300), 2) for _ in years]

    bar = go.Bar(x=years, y=revenue, marker_color='royalblue')
    layout = go.Layout(
        title='Revenue Growth Year to Year',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Revenue (in $k)')
    )
    fig = go.Figure(data=[bar], layout=layout)
    chart = pyo.plot(fig, output_type='div', include_plotlyjs=False)
    return render_template('revenue_growth.html', chart=chart)


@app.route('/audit_risk')
def audit_risk():
    accounts = ['Receivables', 'Revenue', 'Payables', 'Accruals']
    risk_levels = ['High', 'Medium', 'Low']
    risk_map = {'High': 3, 'Medium': 2, 'Low': 1}
    # Randomly assign risk levels and accounting data
    risks = [random.choice(risk_levels) for _ in accounts]
    data = [round(random.uniform(50, 200), 2) for _ in accounts]
    risk_numeric = [risk_map[r] for r in risks]

    bar = go.Bar(x=accounts, y=data, marker_color='orange',
                 name='Accounting Data')
    risk_bar = go.Bar(x=accounts, y=risk_numeric,
                      marker_color='crimson', name='Audit Risk Level')
    layout = go.Layout(
        title='Audit Risk Analysis',
        xaxis=dict(title='Account'),
        yaxis=dict(title='Value / Risk Level'),
        barmode='group'
    )
    fig = go.Figure(data=[bar, risk_bar], layout=layout)
    chart = pyo.plot(fig, output_type='div', include_plotlyjs=False)
    # Pass risk labels for legend
    return render_template('audit_risk.html', chart=chart, risks=zip(accounts, risks))


if __name__ == '__main__':
    app.run(debug=True)
