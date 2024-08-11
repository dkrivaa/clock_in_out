import streamlit as st
from datetime import datetime

import engine

today = datetime.today().date()
now = datetime.now().time()
in_out_options = ['clock-in', 'clock-out']

# Choose clock-in / clock-out
in_out = st.radio(label='Choose', options=in_out_options, index=None)
st.divider()

# Clock-in
if in_out == in_out_options[0]:
    # Choose Customer
    customer = st.selectbox(label='Customer', options=engine.customers(), index=None, placeholder='Choose Customer')
    st.divider()
    # Choose date
    day = st.date_input(label='Enter Date', value=today, max_value=today, format='DD/MM/YYYY')
    st.divider()
    # Choose time
    t = st.time_input('Choose time', step=300, )
    st.divider()
    # Description
    description = st.text_area(label='Enter Description', )

    submit = st.button(label='Submit', type='primary', key='in_key')

    # If new clock-in entry
    if submit and in_out == in_out_options[0] and customer and description:
        data = [customer, day, description, t]
        engine.add_clock_in(data)
    elif submit and in_out == in_out_options[0] and description:
        st.warning('Please Choose Customer')
    elif submit and in_out == in_out_options[0] and customer:
        st.warning('Please Enter Description')
    elif submit and in_out == in_out_options[0]:
        st.warning('Please Choose Customer and Enter Description')

# Clock-out
if in_out == in_out_options[1]:
    df = engine.display_clok_out()
    # Column configuration of displayed dataframe
    column_config = {
        "שעות": {"hidden": True},
    }
    # Add a checkbox column to allow row selection
    df['Select Clock-out'] = [False] * len(df)
    # Configure date display
    df['תאריך'] = df['תאריך'].dt.strftime('%d/%m/%Y')

    df_correct = st.data_editor(df, hide_index=True, use_container_width=True, column_config=column_config)

    # Filter the selected row(s)
    selected_row = df_correct[df_correct['Select Clock-out'] == True]
    row_index = selected_row.index

    if len(row_index) > 0:
        t = st.time_input('Choose clock-out time', step=300, )
        submit = st.button('Submit', type='primary')

        if submit:
            answer = engine.add_clock_out(t, row_index[0])

            st.subheader(answer)




