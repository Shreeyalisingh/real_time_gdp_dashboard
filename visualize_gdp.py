import plotly.graph_objects as go
from fetch_gdp import fetch_gdp_data, compute_growth_rates

def plot_gdp_and_growth():
    df = fetch_gdp_data()
    df = compute_growth_rates(df)

    fig = go.Figure()

    # GDP plot
    fig.add_trace(go.Scatter(
        x=df['year'], y=df['gdp'],
        mode='lines+markers',
        name='GDP (USD)',
        line=dict(color='blue')
    ))

    # GDP growth rate plot
    fig.add_trace(go.Scatter(
        x=df['year'], y=df['growth_rate (%)'],
        mode='lines+markers',
        name='Growth Rate (%)',
        yaxis='y2',
        line=dict(color='green')
    ))

    # Layout
    fig.update_layout(
    title='India GDP and Growth Rate Over Time',
    xaxis_title='Year',
    yaxis=dict(
        title=dict(text='GDP (USD)', font=dict(color='blue')),
        tickfont=dict(color='blue')
    ),
    yaxis2=dict(
        title=dict(text='Growth Rate (%)', font=dict(color='green')),
        overlaying='y',
        side='right',
        tickfont=dict(color='green')
    ),
    legend=dict(x=0.01, y=0.99),
    template='plotly_white'
)


    fig.show()

if __name__ == "__main__":
    plot_gdp_and_growth()
