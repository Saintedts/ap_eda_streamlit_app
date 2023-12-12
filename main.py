import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_option('deprecation.showPyplotGlobalUse', False)


data = pd.read_csv('datasets/main.csv')


st.title('Разведочный анализ данных')


st.subheader('Обзор данных')
st.dataframe(data.drop(columns=['AGREEMENT_RK', 'ID_CLIENT']).head())


st.subheader('Описательная статистика')
st.write(data.drop(columns=['AGREEMENT_RK', 'ID_CLIENT']).describe())


st.subheader('Распределение возраста')
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data, x='AGE', bins=30, kde=True,  ax=ax)
ax.set_xlabel('Возраст')
ax.set_ylabel('Количество людей')
st.pyplot(fig)


st.subheader('Количество клиентов с откликом и без')
st.bar_chart(data['TARGET'].map({1: 'Мужчина', 0: 'Женщина'}).value_counts())


st.subheader('Диаграмма социального статуса по работе')
st.bar_chart(data['SOCSTATUS_WORK_FL'].map(
    {1: 'Не работает', 0: 'Работает', 2: 'Не известно'}).value_counts())


st.subheader('Диаграмма социального статуса по пенсии')
st.bar_chart(data['SOCSTATUS_PENS_FL'].map(
    {1: 'Не пенсионер', 0: 'Пенсионер'}).value_counts())


st.subheader('Диаграмма пола клиентов')
st.bar_chart(data['GENDER'].map(
    {1: 'Мужчина', 0: 'Женщина'}).value_counts())


st.subheader('Количество детей')
st.bar_chart(data['CHILD_TOTAL'].value_counts())


st.subheader('Количество иждивенцев')
st.bar_chart(data['DEPENDANTS'].value_counts())


st.subheader('Количество ссуд')
fig_loan_total, ax_loan_total = plt.subplots(figsize=(10, 6))
loan_total_counts = data['LOAN_NUM_TOTAL'].value_counts()
ax_loan_total.bar(loan_total_counts.index,
                  loan_total_counts,
                  label='Количество ссуд')
ax_loan_total.set_xlabel('Количество ссуд')
ax_loan_total.set_ylabel('Количество клиентов')
st.pyplot(fig_loan_total)


st.subheader('Количество закрытых ссуд')
fig_loan_closed, ax_loan_closed = plt.subplots(figsize=(10, 6))
loan_closed_counts = data['LOAN_NUM_CLOSED'].value_counts()
ax_loan_closed.bar(loan_closed_counts.index,
                   loan_closed_counts,
                   label='Количество закрытых ссуд',
                   color='orange')
ax_loan_closed.set_xlabel('Количество закрытых ссуд')
ax_loan_closed.set_ylabel('Количество клиентов')
st.pyplot(fig_loan_closed)


st.subheader('Тепловая карта корреляции')
heatmap = sns.heatmap(data.corr(numeric_only=True), cmap="YlGnBu", annot=True)
st.pyplot(heatmap.get_figure())


st.subheader('Распределение личного дохода по таргету')
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data, x='PERSONAL_INCOME', hue='TARGET',
             bins=30, kde=True, log_scale=True, ax=ax)
ax.set_xlabel('Личный доход')
ax.set_ylabel('Количество клиентов')
st.pyplot(fig)
