

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt


#ex-2
rand = np.random.normal(1,2,size =20)
fig, ax = plt.subplots()
ax.hist(rand, bins = 15)
st.pyplot(fig)


#ex-1
# Page title
# st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
# st.title('📊 Interactive Data Explorer')

# st.sidebar.title('sidebar title')

# st.title("this is he app title")
# st.header("this is he app header")
# st.markdown("this is he app markdown")
# st.subheader("this is he app subheader")
# st.caption("this is he app caption")
# st.code("x=2021")
# st.latex(r'''a+a r^1+a r^2+a r^3''')

# st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fv.daum.net%2Fv%2F5b4bfe6fed94d2000182d4e3&psig=AOvVaw0BnVVrED_6c6dO-SQQDCK1&ust=1711591313653000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCLDG4NOsk4UDFQAAAAAdAAAAABAE')

# st.checkbox('yes')
# st.button('Click')
# gender = st.radio('pick your gender',['Male','Female'])
# st.selectbox('Pick your gender',['Male','Female'])
# plant = st.multiselect('choose a planet',['jupiter','mars','neptune'])
# st.select_slider('Pick a mark',['Bad','Good','Excellent'])
# st.slider('Pick a number', 0,50)

# st.number_input('Pick a number',0,10)
# st.text_input('Email address')
# st.date_input('travelling data')
# st.time_input('school time')
# st.text_area('description')
# st.file_uploader('Upload a photo')
# st.color_picker('choose your favorite color')
                                 

# with st.expander('About this app'):
#   st.markdown('**What can this app do?**')
#   st.info('This app shows the use of Pandas for data wrangling, Altair for chart creation and editable dataframe for data interaction.')
#   st.markdown('**How to use the app?**')
#   st.warning('To engage with the app, 1. Select genres of your interest in the drop-down selection box and then 2. Select the year duration from the slider widget. As a result, this should generate an updated editable DataFrame and line plot.')
  
# st.subheader('Which Movie Genre performs ($) best at the box office?')

# # Load data
# df = pd.read_csv('data/movies_genres_summary.csv')
# df.year = df.year.astype('int')

# # Input widgets
# ## Genres selection
# genres_list = df.genre.unique()
# genres_selection = st.multiselect('Select genres', genres_list, ['Action', 'Adventure', 'Biography', 'Comedy', 'Drama', 'Horror'])

# ## Year selection
# year_list = df.year.unique()
# year_selection = st.slider('Select year duration', 1986, 2006, (2000, 2016))
# year_selection_list = list(np.arange(year_selection[0], year_selection[1]+1))

# df_selection = df[df.genre.isin(genres_selection) & df['year'].isin(year_selection_list)]
# reshaped_df = df_selection.pivot_table(index='year', columns='genre', values='gross', aggfunc='sum', fill_value=0)
# reshaped_df = reshaped_df.sort_values(by='year', ascending=False)


# # Display DataFrame

# df_editor = st.data_editor(reshaped_df, height=212, use_container_width=True,
#                             column_config={"year": st.column_config.TextColumn("Year")},
#                             num_rows="dynamic")
# df_chart = pd.melt(df_editor.reset_index(), id_vars='year', var_name='genre', value_name='gross')

# # Display chart
# chart = alt.Chart(df_chart).mark_line().encode(
#             x=alt.X('year:N', title='Year'),
#             y=alt.Y('gross:Q', title='Gross earnings ($)'),
#             color='genre:N'
#             ).properties(height=320)
# st.altair_chart(chart, use_container_width=True)
