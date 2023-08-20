### ===============
import pandas as pd

# pip install streamlit
import streamlit as sl

from PIL import Image

#from sklearn import datasets
#iris = datasets.load_iris()

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

import seaborn as sb

import numpy as np

from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import row
from bokeh.plotting import figure, show
#output_notebook()
from bokeh.palettes import Category20c
from bokeh.transform import cumsum

from math import pi

# pip install statsmodels
from statsmodels import robust

from pathlib import Path
import random

from scipy import stats
import statsmodels.api as sm
from scipy.stats import mannwhitneyu

import statsmodels.formula.api as smf
from statsmodels.stats import power
### ===============

### ===============
def begin_Visualization():
    sl.caption("**Version:** _0.3_")
    
    ###
    sl.caption("Innopolis University Logotypes:")
    
    #col_0, col_1 = sl.columns(2, gap = "large")
    col_0, col_1 = sl.columns([1, 1], gap = "large")
    
    with col_0:
        #logo_1 = Image.open("logo_1.png")
        # w = 431, h = 101
        #sl.image(logo_1, caption = "")
        
        # ! Сделать выравнивание по нижнему краю
        #placeholder = sl.empty()
        sl.caption("")
        sl.caption("")
        sl.caption("")
        sl.caption("")
        sl.caption("")
        sl.caption("")
        sl.caption("")
        sl.caption("")
        
        sl.image("https://upload.wikimedia.org/wikipedia/commons/4/48/ЛОГОТИП_УИ.svg", caption = "New")
        #, width = 431)
    
    with col_1:
        logo_0 = Image.open("logo_0.png")
        # w = 1338, h = 813
        sl.image(logo_0, caption = "Old") #, width = 134)

    ###
    sl.write("---") # or "---" (only in StreamLit)

    ###
    sl.title("Промежуточная аттестация № _1_")

    ###
    sl.markdown("**Ф. И. О.:** _Cенчило П. В._;")
    sl.markdown("**ПА** №: `001` = **Блок** № `1`;")
    sl.markdown("**Дата:** `2023-08-15`.")

    ###
    #sl.image("https://upload.wikimedia.org/wikipedia/commons/8/83/Iris_germanica_160505.jpg", 
    #caption = "Iris Germanica")

    ###
    sl.divider()

### ===============
def load_DF():
    spoiler = "Expand / Collapse ..."
    
    ###
    sl.markdown("**_Iris_ Data-Set Link:** https://www.kaggle.com/datasets/uciml/iris")
    sl.text("... or...")
    sl.code(body = "from sklearn import datasets \niris = datasets.load_iris()", language = "python", line_numbers = True)
    sl.code(body = "$ streamlit run _.py", language = "python", line_numbers = True)
    sl.divider()
    
    ### === 0. UpLoading a File:
    # Limit 200MB per file. File must be 200.0MB or smaller.
    sl.header("Step _1_. 📎")
    f_uploaded = sl.file_uploader("**Please, pick a Data-Set-containing File:**")
    if (f_uploaded is not None):
        # To See File Details:
        f_details = {
            "File Name": f_uploaded.name, 
            "File Type": f_uploaded.type,
            "File Size": f_uploaded.size } # (байт)
        sl.write("**The Picked File Details:**")
        sl.write(f_details)
        sl.write("**- [File] MIME-Type:**", f_details["File Type"], "=", f_uploaded.type)
        f_type = f_uploaded.type
        
        #
        #sl.write("**-- [MIME-Type]: Name Type & Supported Methods:**")
        #with sl.expander(spoiler, expanded = False):
        #    sl.write(type(f_type))
        #

    ### === 1. Checking the File Type:
        if (f_type != "text/csv"):
            sl.write(":red[**InPut Error:** Please, select a CSV-File instead!]")
            sl.markdown(":red[**UnicodeDecodeError:** 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte]")
        else:
            sl.write(":green[**InPut's OK:** The CSV-File with Data-Set has been uploaded successfully]")
        
        ### === 2. Viewing the DataSet:

            ### A. Pandas Data-Frame:
            #DS_f_name = "data_sets/Iris.csv" #
            #sl.text("The Selected Data-Set [CSV-File] Path + Name = " + DS_f_name) #
            #DF_PD = pd.read_csv(DS_f_name)
            
            ###
            #sl.subheader("A. ) Pandas Data-Frame OutPut:")
            #with sl.expander(spoiler, expanded = True):
            #    DF_PD
            
            ### B. StreamLit Data-Frame (Pandas):
            # Can be used wherever a "file-like" object is accepted:
            DF_SL = pd.read_csv(f_uploaded)
            #DF_SL = sl.dataframe(data = f_uploaded)
            
            ###
            sl.subheader("B. Streamlit Data-Frame OutPut Methods:")
            with sl.expander(spoiler, expanded = False):
                col_a = "DataFrame"
                col_b = "Write"
                col_c = "Table"
                tab_a, tab_b, tab_c = sl.tabs([col_a, col_b, col_c])
                
                with tab_a:
                    sl.subheader("_.a) `" + col_a + "`:")
                    sl.dataframe(DF_SL)
                
                with tab_b:
                    sl.subheader("_.b) `" + col_b + "`:")
                    sl.write(DF_SL)
                
                with tab_c:
                    sl.subheader("_.c) `" + col_c + "`:")
                    sl.table(DF_SL)
            
            ###
            DF_cols_names = list(DF_SL.columns.values) #list(DF_PD)
            sl.write("**Data-Frame Columns' Names:**", DF_cols_names)
            # = ["Id", "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]
            DF_cols_num = len(DF_cols_names)
            sl.write("**=> Всего столбцов:**", DF_cols_num)
            DF_rows_num = len(DF_SL)
            sl.write("**=> Всего строк:**", DF_rows_num)
            
            ###
            #DF_cols_ru = ["№ ", "Д.( Ч.) (см)", "Ш.( Ч.) (см)", "Д.( Л.) (см)", "Ш.( Л.) (см)", "Виды рода Ирис"]
            #sl.write("**Перевод их названий:**")
            #sl.write("// (Д. = Длина, Ш. = Ширина; Ч. = Чаше-листик, Л. = Лепесток)", DF_cols_ru)
            
            ###
            select_DF_cols(DF_SL, DF_cols_names)

### ===============
def select_DF_cols(DF, DF_cols_names): 
    sl.divider()
    
    ### === 0. Selecting Data-Frame Columns:       
    sl.header("Step _2_. ☑️")
    sl.write("**Please, select _2_ Data-Frame Columns, _1_ by _1_:**")

    ### = Multi-Selection:
    sl.write("// Просто для примера использования метода `MultiSelection`:")
    sel_col_1, sel_col_2 = sl.multiselect(label = "**Columns** №№ _1_ & _2_:", options = DF_cols_names, default = [DF_cols_names[1], DF_cols_names[2]], max_selections = 2, placeholder = "Choose _2_ Columns", disabled = True, label_visibility = "visible") # 
    # ValueError: not enough values to unpack (expected 2, got 0)

    sl.write("// Для демонстрации изначально специально выбраны _2_ одинаковые колонки.")
    sl.write("// Чтобы не тратить лишнее время на ожидание построения графиков по столбцу `Id`, ")
    sl.write("//  в верхнем правом углу приложения можно нажать на кнопку `Stop` ")
    sl.write("//  и сразу выбрать другой (более подходящий) столбец.")
    
    ### = Drop-Down _1_
    sel_col_1_name = sl.selectbox(label = "**Column** № _1_:", options = DF_cols_names)#, key = "c1")
    
    #sl.write(type(sel_col_1_name)) # => load_DF() classbuiltins.str(...)
    
    ### = Drop-Down _2_
    sel_col_2_name = sl.selectbox(label = "**Column** № _2_:", options = DF_cols_names, index = 0)#, key = "c2")

    sl.write("**Your selected Columns:**", sel_col_1_name, "&", sel_col_2_name)
    
    ### === 1. Checking if they are not the same:
    if (sel_col_1_name == sel_col_2_name):
        sl.write(":red[**InPut Error:** Please, select _2_ different Data-Frame Columns (change _1_ of them)!]")
    else:
        sl.write(":green[**InPut's OK:** The _2_ selected Data-Frame Columns are different]")
        plot_Distribution(DF, DF_cols_names, sel_col_1_name, sel_col_2_name) 

### =============== ===============
def is_Categorial(DF, sel_col_name): 
    # datetime = ?
    T_cat_types = ("category", "object", "string")
    F_cat_types = ("float", "float64")
    X_cat_types = ("int", "int64")
    
    DF_cols_names = list(DF.columns.values) # Заново!
    sel_col_i = DF_cols_names.index(sel_col_name)
    sel_col_type = DF.dtypes[sel_col_i].name
    sl.write("**Column** [", sel_col_name, "] **Type** is:", sel_col_type)   

    sl.write("=> Column [", sel_col_i, "] Values are:")
    if (sel_col_type in F_cat_types):
        is_cat_sel_col = False
        sl.write("Not Categorical.")
    elif (sel_col_type in T_cat_types):
        is_cat_sel_col = True
        sl.write("    Categorical.")
    else:
        is_cat_sel_col = True #
        sl.write("??? Categorical.")
    return is_cat_sel_col

### =============== ===============
def if_Charts_or_Hist(DF, sel_col_name, is_cat_sel_col):
    if (is_cat_sel_col == True):
        plot_Charts(DF, sel_col_name)
    elif (is_cat_sel_col == False):
        plot_Hist(DF, sel_col_name)
 
### =============== ===============
def plot_Charts(DF, sel_col_name):
    sl.write("**=> Plot _2_ Charts:**", sel_col_name)
 
    sl.write("**:orange[Графики `Bokeh` открываются в новых отдельных вкладках (`Bokeh Plot`)!]**")
    sl.code(body = "file:///C:/Temp/_.html", language = "python", line_numbers = True) 
 
    ### 1. Столбчатая Диаграмма
    
    # 4.2 = SeaBorn 2
    sb_bar = sb.countplot(x = sel_col_name, data = DF)
    plt.title("Столбчатая Диаграмма (SeaBorn)")
    #plt.show()
    sl.pyplot()
    
    # 5.0 = Bokeh
    values = list(set(DF[sel_col_name]))
    counts = DF[sel_col_name].value_counts()
    p = figure(x_range = values, height = 350, title = "Столбчатая Диаграмма (Bokeh)", toolbar_location = None, tools = "")
    p.vbar(x = values, top = counts, width = 0.8)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    show(p)    
    ######
    
    ### 2. Круговая Диаграмма
    # 1.1 = Pandas 1
    pd_pie = DF[sel_col_name].value_counts().plot(kind = 'pie', figsize = (6, 6), autopct = '%1.2f%%')
    plt.title("Круговая Диаграмма (Pandas)")
    plt.xlabel("")
    plt.ylabel("") 
    #plt.show()
    sl.pyplot()
    
    # 5.0 = Bokeh
    pd_ser = DF[sel_col_name].value_counts()#.values = [50 50 50], <class 'numpy.ndarray'>
    sl.write(pd_ser)
    #spoiler = "Expand / Collapse ..."
    #with sl.expander(spoiler, expanded = False):    
    #    sl.write("Type of [pd_ser]:", type(pd_ser))
    data = pd_ser.reset_index(name = 'value').rename(columns = {'index': 'Species'}) #
    data['angle'] = ( data['value']/data['value'].sum() ) * 2*pi
    data['color'] = Category20c[len(pd_ser)]
    p = figure(height = 350, title = "Pie Chart (Bokeh)", toolbar_location = None,
               tools = "hover", tooltips = "@Species: @value", x_range = (-0.5, 1.0)) #
    p.wedge(x = 0, y = 1, radius = 0.4, 
            start_angle = cumsum('angle', include_zero = True), end_angle = cumsum('angle'),
            line_color = "white", fill_color = 'color', legend_field = 'Species', source = data) #
    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None
    show(p)    
    ######
    
    #sl.write("**:orange[Графики `Bokeh` открываются в новых отдельных вкладках (`Bokeh Plot`)!]**")
    #sl.code(body = "file:///C:/Temp/_.html", language = "python", line_numbers = True)    
    ######
    
### =============== ===============
def plot_Hist(DF, sel_col_name): # DF_rows_num
    sl.write("**=> Plot _a_ Hist:**", sel_col_name)
    DF_rows_num = len(DF) # = Заново!
    
    ### 0. Гистограмма 
    # 2.1 = MatPlotLib 1
    mpl_hist = plt.hist(DF[sel_col_name], bins = DF_rows_num)
    plt.title("Гистограмма (MatPlotLib)")
    plt.xlabel(sel_col_name)
    plt.ylabel("Частота")
    #plt.show()
    sl.pyplot()
    
    sl.text("Data_Frame[sel_col_name]:\n")
    sl.text(DF.describe()[sel_col_name])

### ===============    
def plot_Distribution(DF, DF_cols_names, sel_col_1_name, sel_col_2_name):
    sl.divider()
    
    ### === 0. Viewing the selected Data-Frame Columns' Types:
    sl.header("Step _3_. 📊")
    sl.write("**Plotting the selected Data-Frame Columns' Data:**")
    
    sl.write("**All of the Data-Frame Columns' Types:**")
    sl.text(DF.dtypes)
    
    ### === 1. Checking if the selected Columns are Categorical or non-:
    
    #sel_col_1_i = DF_cols_names.index(sel_col_1_name)
    is_cat_sel_col_1 = is_Categorial(DF, sel_col_1_name)
    
    #sel_col_2_i = DF_cols_names.index(sel_col_2_name)
    is_cat_sel_col_2 = is_Categorial(DF, sel_col_2_name)
    
    ### === 2. Depending on if they are Categorical, plot a Bar-Chart or a HistoGram:
    sl.set_option('deprecation.showPyplotGlobalUse', False)
    sl.write("- - -")
    sl.write("**1.**")
    if_Charts_or_Hist(DF, sel_col_1_name, is_cat_sel_col_1)
    sl.divider()
    sl.write("**2.**")
    if_Charts_or_Hist(DF, sel_col_2_name, is_cat_sel_col_2)
    # -->
    summary_1()
    
    # -->
    stat_hip(DF, sel_col_1_name, sel_col_2_name)  

### ===============
def summary_1():
    sl.divider()
    sl.markdown(body = "**Выводы (1):**")
    sl.markdown(body = "**0. Исходные данные**")
    sl.markdown(body = "В качестве примера возьмём **DataSet** `Iris`")
    sl.markdown(body = " и, в частности, выберем его **столбцы** `SepalLengthCm` (Длина чашелистика, см) и `Species` (Виды).")
    sl.markdown(body = "(Нет смысла анализировать **столбец** `Id`, т. к. он содержит просто уникальные номера строк")
    sl.markdown(body = " (описание конкретного, отдельно взятого растения, принадлежащего роду Ирис.)")
    sl.markdown(body = "Всего в этом наборе данных -- `6` **столбцов** и `150` **строк**.")
    sl.markdown(body = "**1. Категориальность**")
    sl.markdown(body = "Значения `SepalLengthCm` -- не категориальные (числа), т. к. это -- непрерывные случайные величины,") 
    sl.markdown(body = " а `Species` -- наоборот, категориальные (строки), т. к. они -- прерывные (дискретные).")
    sl.markdown(body = "**2. Распределения:**")
    sl.markdown(body = "Соответственно, для категориальных колонок строим гистограмму распределения, ")
    sl.markdown(body = " а для не_категориальных -- столбчатую или круговую диаграмму.")
    sl.markdown(body = "**2.1. `SepalLengthCm`**")
    sl.markdown(body = "По гистограмме видно, что **значение длины чашелистика**:")
    sl.markdown(body = "- **среднее**      -- `равное примерно` `5.84(3333)` сантиметрам, ")
    sl.markdown(body = "- **минимальное**  -- `равно` `4.3` см;")
    sl.markdown(body = "- **максимальное** -- `равно` `7.9` см.")
    sl.markdown(body = "**2.2. `Species`**")
    sl.markdown(body = "По диаграммам видно, что в таблице присутствуют ирисы всего `3`х видов,")
    sl.markdown(body = " и каждый из них представлен здесь `ровно` ") 
    sl.latex(body = "150/3 = 50")
    sl.markdown(body = " раз, что составляет $33.(3)$ % от `100`. ")

### ===============
def u_test(DF, sel_col_A_name, sel_col_B_name):
# 3. Mann-Whitney U-test
    sl.divider()
    ##
    is_cat_sel_col_A = is_Categorial(DF, sel_col_A_name)
    is_cat_sel_col_B = is_Categorial(DF, sel_col_B_name)
    if ((is_cat_sel_col_A or is_cat_sel_col_B) == True):
        sl.write(":red[**InPut Error:** Please, select both non-Categorical Data-Frame Columns of the _2_!]")
    else:
    ####
        #sel_col_A_name = DF_cols_names[sel_col_A_i]
        sl.write("Column A =", sel_col_A_name)
        vals_A = DF[sel_col_A_name]

        #sel_col_B_name = DF_cols_names[sel_col_B_i]
        sl.write("Column B =", sel_col_B_name)
        vals_B = DF[sel_col_B_name]

        stat, p_value = mannwhitneyu(vals_A,  vals_B)
        sl.write(f"=> **Mann-Whitney U-Test:** \n - **statistic** \t= {stat:.4f}, \n - **p-value** \t= {p_value:.4f};")

### ===============

def chisq_test(DF, sel_col_A_name, sel_col_B_name):
# 5. Chi-Square-test
    sl.divider()
    ##
    is_cat_sel_col_A = is_Categorial(DF, sel_col_A_name)
    is_cat_sel_col_B = is_Categorial(DF, sel_col_B_name)
    if ((is_cat_sel_col_A or is_cat_sel_col_B) == True):
        sl.write(":red[**InPut Error:** Please, select both non-Categorical Data-Frame Columns of the _2_!]")
    else:
    ####
        #sel_col_A_name = DF_cols_names[sel_col_A_i]
        sl.write("Column A =", sel_col_A_name)
        vals_A = DF[sel_col_A_name]

        #sel_col_B_name = DF_cols_names[sel_col_B_i]
        sl.write("Column B =", sel_col_B_name)
        vals_B = DF[sel_col_B_name]

        data = [vals_A, vals_B]
        chisq, pvalue, df, expected = stats.chi2_contingency(data)
        sl.write(f"=> Chi-Square Test: \n - Observed Chi-Square \t= {chisq:.4f}, \n - p-value \t\t= {pvalue:.4f};")
        # + Resampled p-value = ???

### ===============
def stat_hip(DF, sel_col_1_name, sel_col_2_name):
    sl.divider()
    sl.header("Steps _4-5_. ❔")
    sl.write("**Using Hypothesis Testing Algorithms:**")    
    sl.text("...")
    
    test_1_name = "Mann-Whitney U-Test"
    test_2_name = "Chi-Square Test"
    tests_names_list = [test_1_name, test_2_name]
    
    ### = Drop-Down _1_
    sel_test_name = sl.selectbox(label = "**Test:**", options = tests_names_list)
    if (sel_test_name == test_1_name):
        u_test(DF, sel_col_1_name, sel_col_2_name)
    elif (sel_test_name == test_2_name):
        chisq_test(DF, sel_col_1_name, sel_col_2_name)

### ===============
def summary_2():
    sl.divider()
    sl.markdown(body = "**Выводы (2):**")
    sl.markdown(body = "**0.0 Гипотезы:**")
    sl.markdown(body = "- $H_0$ **(_0_-я):**          _2_ переменные независимы;")
    sl.markdown(body = "- $H_1$ **(альтернативная):** _2_ переменные не являются независимыми.")
    sl.markdown(body = "**0.1 Тесты:**")
    sl.markdown(body = "- **U-критерий Манна-Уитни (= Критерий суммы рангов Уилкоксона)** **возвращает значения**:")
    sl.markdown(body = "-- `statistic`: The Mann-Whitney U statistic corresponding with sample x.")
    sl.markdown(body = "-- `pvalue`: The associated p-value for the chosen alternative.")
    sl.markdown(body = "- **Критерий согласия Пирсона (= Тест $χ^2$, на независимость)** **возвращает значения**:")
    sl.markdown(body = "-- `statistic`: The test statistic.")
    sl.markdown(body = "-- `pvalue`: The p-value of the test.")
    sl.markdown(body = "-- `dof`: The degrees of freedom.")
    sl.markdown(body = "-- `expected_freq`: The expected frequencies, based on the marginal sums of the table.")
    sl.markdown(body = "**=>**")
    sl.markdown(body = "`p-value` -- это вероятность увидеть в наблюдениях разницу между группами.")
    sl.markdown(body = "- Если `p`-значение теста `не меньше` (т. е. `больше равно`) `0,05`, мы не можем отвергнуть `0`-ю гипотезу.")
    sl.markdown(body = "(Это означает, что у нас нет достаточных доказательств, чтобы сказать, что существует связь между `2`мя переменными.)")
    sl.markdown(body = "- И наоборот: если `p`-значение `меньше` `0,05`, мы точно отвергаем `0`-ю гипотезу.")
    
    sl.text("...")
    
### ===============
def main():
    begin_Visualization()
    load_DF() 
    # <-- select_DF_cols(DF, DF_cols_names);
    # <-- plot_Distribution();
    # <-- if_Charts_or_Hist(DF, sel_col__name, is_cat_sel_col);
    # <-- plot_Charts(DF, sel_col_name) || plot_Hist(DF, sel_col_name) ;
    # <-- summary_1();
    # <-- stat_hip();
    # <-- u_test(DF, sel_col_A_name, sel_col_B_name) / ;
    summary_2(); #

main()