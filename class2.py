import streamlit as st
from PIL import Image
import time



st.title('Streamlit methods')

numb = st.number_input('Give some value:: ',)

st.write('square root of above number is ',numb**0.5)

name = st.text_input('Please enter your name:: ')

review = st.text_area('comments:: ')

count = 0
for i in review:
    if i.lower() in "aeiou":
        count += 1

st.write(f'you have used {count} number of vowel characters')

st.divider()

birth_date = st.date_input('Please provide your birth date::')

st.write('Happy birthday on ',birth_date)

st.divider()

date_time = st.datetime_input('Please mention time you wish to :: ')

st.write("favoirate time for death:: ",date_time)

st.divider()

st.write('what is your coursse name at innomatics?')

ans = st.selectbox('Options::',['Data science','Data Analytics','Gen AI'])

st.write(f'congrats for taking {ans} course at innomatics')

####################################multiselect

pic = Image.open(r"https://cdn.navalapp.com/uploads/2024/06/introduction_to_python_course_thumbnail.jpg")

st.image(pic)

##########################################################################################vedio

vedio_file = open(r"https://www.bing.com/videos/riverview/relatedvideo?q=python+video+tutorial&mid=EFA2660E5CC1A916CF09EFA2660E5CC1A916CF09&churl=https%3a%2f%2fwww.youtube.com%2fchannel%2fUCw5tc0QKLXsSnfQIP2XUjww&FORM=VIRE



                  st.video(vedio_file)
############################################################################################audio


    mass = st.empty()

    count = 10

    while count:

        mass.text(f'the bomb is going to blast in {count} secs')
        time.sleep(1)
        count -= 1

    mass.write('Boom.....')  

######################################################################
def progress_bar():
    pgb = st.progress(100)
    ms = st.empty()

    for i in range(1,101):
        pgb.progress(i)
        ms.info(f'{i}% downloded')
        time.sleep(0.1)

    ms.info('downloding completed')

###########################################################################