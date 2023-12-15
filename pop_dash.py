import pandas as pd  
import plotly.express as px  
import streamlit as st  

def main():

    st.set_page_config(page_title="BSKY (Biju Swastya Kalyan Yojana)", page_icon="👨‍⚕️", layout="wide")

    df=pd.read_csv("health_data.csv",  encoding='latin-1')

    st.title('BSKY Dashboards')


    st.sidebar.header("Please Filter Here:")
    dist = st.sidebar.multiselect(
        "Select the District:",
        options=df["District"].unique(),
        default=df["District"].unique()
    )

    df_selection = df.query(
        "District == @dist "
    )

    #checking if the data selection of district is empty
    if df_selection.empty:
        st.warning("No data available based on the current filter settings!")
        st.stop() 



    #creating  dashboards

    total_dist=  int(df_selection["District"].nunique())  
    total_pop = int(df_selection["Population"].sum())
    total_card_pop = int(df_selection["card_holders"].sum())

    perc = round( ( (total_card_pop/total_pop)*100 ),2 );

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")


    st.markdown(
        f'''
        <div style="width:300px; margin:auto; border: 1px solid #000;text-align: center;border-radius:50%;
                        background: linear-gradient(to right top, #1cd1c4, #51c88a, #88b94a, #bba10a, #eb7d12);">
            <h2 style="text-decoration: underline;">Total Districts</h2> <br>
                <h5 style="color:brown;"><strong>{total_dist}</strong></h5>,

        </div>
        ''',
        unsafe_allow_html=True
    )

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    # Creating a fixed-size div box
    st.markdown(
        f''' 
        <div style="width:500px; margin:auto; border: 1px solid #000;text-align: center;border-radius: 20px;background: linear-gradient(to right, #ff6b6b, #6b6bff)">
            <h2 style="color:brown;text-decoration: underline;">Districts: Total Population</h2> <br>
                <h4>Total</h4> 
                <p>----------------------</p>
                <h5 style="color:green;"><strong>{total_pop}</strong></h5>,

        </div>
        ''',
        unsafe_allow_html=True
    )

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")


    st.markdown(
        f'''
        <div style="width:500px; margin:auto; border: 1px solid #000;text-align: center;border-radius: 20px;background: linear-gradient(to right top, #053712, #28621d, #548f23, #8abd21, #caeb12);">
            <h2 style="text-decoration: underline;">Districts: Total Card Holders</h2> <br>
                <h4 style="color:brown;">Total</h4> 
                <p>----------------------</p>
                <h5 style="color:blue;"><strong>{total_card_pop}</strong></h5>,

        </div>
        ''',
        unsafe_allow_html=True
    )

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    st.markdown(
        f'''
        <div style="width:500px; margin:auto; border: 1px solid #000;text-align: center;border-radius: 50%;background: linear-gradient(to right top, #a5b21d, #db8f00, #ff5f3e, #ff287f, #dd35c8);
                    word-wrap: break-word; "> <br>
            <h2 style="color:brown;text-decoration: underline;">Total % of card holders</h2> <br>
                <h4>Total</h4> 
                <p>----------------------</p>
                <h5 style="color:blue;"><strong>{perc}</strong> %</h5>,

        </div>
        ''',
        unsafe_allow_html=True
    )

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")



    if 'District' in df.columns and 'Population' in df.columns:
            # Creating a bar chart using Plotly Express
            fig = px.bar(df, x='District', y='Population', title='District Total Population Bar Chart', color='District',
                            color_discrete_map={'red': 'red', 'green': 'green', 'blue': 'blue', 'orange': 'orange'})
            st.plotly_chart(fig)
    else:
            st.warning("CSV file must contain 'District' and 'Population' columns.")

    
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    
    if 'District' in df.columns and 'card_holders' in df.columns:
           
            fig2 = px.bar(df, x='District', y='card_holders', title='District Card Holders Population Bar Chart', color='District',
                            color_discrete_map={'red': 'red', 'green': 'green', 'blue': 'blue', 'orange': 'orange'})
            st.plotly_chart(fig2)
    else:
            st.warning("CSV file must contain 'District' and 'Card Holders' columns.")


    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    if 'District' in df.columns and 'Population' in df.columns:
            fig3 = px.pie(df, values='Population', names='District', title='District Total Population Pie Chart')
            st.plotly_chart(fig3)
    else:
            st.warning("CSV file must contain 'District' and 'Population' columns.")

    
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    if 'District' in df.columns and 'card_holders' in df.columns:
            fig4 = px.pie(df, values='card_holders', names='District', title='District Total Card Holders Pie Chart')
            st.plotly_chart(fig4)
    else:
            st.warning("CSV file must contain 'District' and 'Card Holders' columns.")


    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")



    if 'District' in df.columns and 'Population' in df.columns:
            fig5 = px.line(df, x='District', y='Population', title='District Total Population Line Chart')
            st.plotly_chart(fig5)
    else:
            st.warning("CSV file must contain 'District' and 'Population' columns.")

    
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    
    if 'District' in df.columns and 'card_holders' in df.columns:
           
            fig6 = px.line(df, x='District', y='card_holders', title='District Card Holders Population Line Chart')
            st.plotly_chart(fig6)
    else:
            st.warning("CSV file must contain 'District' and 'Card Holders' columns.")



    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    if 'District' in df.columns and 'Population' in df.columns and 'Latitude' in df.columns and 'Longitude' in df.columns:
            
            fig7 = px.scatter_geo(
                df,
                lat='Latitude',
                lon='Longitude',
                size='Population',
                hover_name='District',
                title='District Population Map',
                projection='equirectangular'
            )

            
            st.plotly_chart(fig7)
    else:
            st.warning("CSV file must contain 'District', 'Population', 'Latitude', and 'Longitude' columns.")




if __name__ == '__main__':
    main()







