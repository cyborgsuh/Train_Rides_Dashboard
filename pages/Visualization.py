import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit_shadcn_ui as ui

st.set_page_config(layout="wide")


df=pd.read_csv(r".\railway.csv")

def ticket_sales_over_time(df):
    df['Date of Purchase'] = pd.to_datetime(df['Date of Purchase'])
    df_count = df.groupby('Date of Purchase').size().reset_index(name='Ticket Count')
    fig = px.line(df_count, x='Date of Purchase', y='Ticket Count', title='Ticket Sales Over Time', line_shape='spline')
    fig.update_layout(xaxis_title='Date of Purchase', yaxis_title='Ticket Sales (Count)')
    fig.update_layout(
        title={
            'font': {'size': 24},  
            'x': 0.5,  
            'xanchor': 'center' 
        },
        
    )
    fig.update_traces(line=dict(color='#D1B7A1'))  
    return fig

def payment_method_distribution(df):
    df_payment_method_count = df['Payment Method'].value_counts().reset_index(name='Ticket Count').rename(columns={'index': 'Payment Method'})
    fig = px.pie(df_payment_method_count, names='Payment Method', values='Ticket Count', title='Payment Method',color_discrete_sequence=['#D1B7A1', '#ead7bb', '#c9a78e'])
    fig.update_layout(
        title={
            'font': {'size': 24},  
            'x': 0.5,  
            'xanchor': 'center'  
        }
    )
    return fig




# Bar chart for delayed journeys by Departure Station
def delays_by_station(df):
    delayed_df = df[df['Journey Status'] == 'Delayed']
    delay_by_station = delayed_df.groupby('Departure Station').size().reset_index(name='Count')
    fig = px.bar(delay_by_station, x='Departure Station', y='Count',
                 title='Delays by Departure Station',
                 labels={'Departure Station': 'Station', 'Count': 'Number of Delays'},
                 color='Count',
                 color_continuous_scale=['#ead7bb','#D1B7A1' ])
    fig.update_layout(xaxis={'categoryorder': 'total descending'},coloraxis_showscale=False,)  # Sort by delay count
    fig.update_layout(
        title={
            'font': {'size': 24},  
            'x': 0.5,  
            'xanchor': 'center'  
        }
    )
    return fig

# Line chart for refund request trends over time
def refund_request_trends(df):
    refund_trends = df[df['Refund Request'] != 'No'].groupby('Date of Purchase').size().reset_index(name='Count')
    fig = px.line(refund_trends, x='Date of Purchase', y='Count',
                  title='Refund Request Trends Over Time',
                  labels={'Date of Purchase': 'Date of Purchase', 'Count': 'Number of Refund Requests'},
                  line_shape='spline',
                  color_discrete_sequence=['#D1B7A1'],
                  )
    fig.update_traces(mode='lines+markers')  # Add markers to the line chart
    fig.update_layout(
        title={
            'font': {'size': 24},  
            'x': 0.5,  
            'xanchor': 'center'  
        },
        height=917,  # Match the combined height of the two charts in col3
        margin=dict(t=300, b=300,l=20,r=20),  # Adjust margins

    )
    return fig

def ticket_purchase_density(df):
    df['Day of Week'] = pd.to_datetime(df['Date of Purchase']).dt.day_name()
    df['Hour of Day'] = pd.to_datetime(df['Time of Purchase'], format='%H:%M:%S').dt.hour
    heatmap_data = df.groupby(['Day of Week', 'Hour of Day']).size().reset_index(name='Ticket Count')
    heatmap_pivot = heatmap_data.pivot(index='Day of Week', columns='Hour of Day', values='Ticket Count').fillna(0)

    fig = go.Figure(data=go.Heatmap(
        z=heatmap_pivot.values,
        x=heatmap_pivot.columns,
        y=heatmap_pivot.index,
        colorscale=[[0, '#D1B7A1'], [0.2, '#ead7bb'], [0.4, '#F5CBA7'], [0.6, '#FAD02E'], [1, '#F28D35']],  # sandy theme colors
        colorbar=dict(title='Ticket Count')
    ))

    for i, day in enumerate(heatmap_pivot.index):
        for j, hour in enumerate(heatmap_pivot.columns):
            fig.add_annotation(
                x=hour,
                y=day,
                text=str(int(heatmap_pivot.loc[day, hour])),
                showarrow=False,
                font=dict(color='white' if heatmap_pivot.loc[day, hour] > heatmap_pivot.values.max() / 2 else 'black'),
                align='center'
            )

    fig.update_layout(
        title='Ticket Purchase Density by Time and Day',
        xaxis=dict(title='Hour of Day'),
        yaxis=dict(title='Day of Week'),
        height=800,
        width=1500
    )
    fig.update_layout(
        title={
            'font': {'size': 24},
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    return fig

# Bar chart for ticket type distribution by railcard holders
def ticket_type_distribution_by_railcard(df):
    railcard_distribution = df.groupby(['Railcard', 'Ticket Type']).size().reset_index(name='Ticket Count')
    fig = px.bar(railcard_distribution, x='Railcard', y='Ticket Count', color='Ticket Type',
                 title="Ticket Type Distribution by Railcard Holders",
                 labels={'Ticket Count': 'Number of Tickets', 'Railcard': 'Railcard Holder', 'Ticket Type': 'Type of Ticket'},
                 color_discrete_sequence=['#D1B7A1', '#ead7bb', '#c9a78e'])
    fig.update_layout(
        title={
            'font': {'size': 24},  
            'x': 0.5,  
            'xanchor': 'center'  
        }
    )
    return fig


# Create Streamlit page layout
st.title('Ticket Data Insights')


total_tickets_sold = df.shape[0]  # Total number of tickets
total_refunds = df[df['Refund Request'] != 'No'].shape[0]  # Count of refund requests
total_delays = df[df['Journey Status'] == 'Delayed'].shape[0]  # Count of delayed journeys
refund_rate = (total_refunds / total_tickets_sold) * 100  # Refund rate as a percentage

# Create 4 columns for the metrics cards
col1, col2, col3, col4 = st.columns(4)

# Column 1: Total Tickets Sold
with col1:
    ui.metric_card(
        title="Total Tickets Sold",
        content=f"{total_tickets_sold:,}",
        description="Overall Sales in Last Month"
    )

# Column 2: Total Refunds
with col2:
    ui.metric_card(
        title="Total Refunds",
        content=f"{total_refunds:,}",
        description="Refund Requests Processed"
    )

# Column 3: Total Delays
with col3:
    ui.metric_card(
        title="Total Delays",
        content=f"{total_delays:,}",
        description="Delayed Journeys"
    )

# Column 4: Refund Rate
with col4:
    ui.metric_card(
        title="Refund Rate",
        content=f"{refund_rate:.2f}%",
        description="Percentage of Refunds"
    )


col1, col2 = st.columns([3, 1])

with col1:
    with st.container(border=True):
        st.plotly_chart(ticket_sales_over_time(df))

with col2:
    with st.container(border=True):
        st.plotly_chart(payment_method_distribution(df))


# Second row layout (Ticket Type Distribution and Delays by Station)
col3, col4 = st.columns([2, 4])

with col3:
    with st.container(border=True):
        st.plotly_chart(ticket_type_distribution_by_railcard(df))
        st.plotly_chart(delays_by_station(df))

with col4:
    with st.container(border=True):
        st.plotly_chart(refund_request_trends(df), use_container_width=True)  # This ensures it takes full width


# Third row layout (Heatmap)
with st.container(border=True):
    st.plotly_chart(ticket_purchase_density(df), use_container_width=True)





