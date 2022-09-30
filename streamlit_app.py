import streamlit as st
from PIL import Image
#from streamlit_timeline import timeline
#st.set_page_config(page_title="Timeline Example", layout="wide")
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#space, app, space = st.columns ([1,5,1])

#with app:
#####################
# Header 
# st.write('''
# # Sanchit Goel
# ##### *Resume* 
# ''')

# image = Image.open('dp.png')
# st.image(image, width=150)

# st.markdown('''
# <iframe src="https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=1xuY4upIooEeszZ_lCmeNx24eSFWe0rHe9ZdqH2xqVNk&font=Default&lang=en&initial_zoom=2&height=100%" width="100%" frameborder="0"></iframe>''', unsafe_allow_html = True)
                                
# st.markdown('## Summary', unsafe_allow_html=True)
# st.info('''
# - Experienced Educator, Researcher and Administrator with almost twenty years of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
# - Strong verbal and written communication skills as demonstrated by extensive participation as invited speaker at `10` conferences as well as publishing 149 research articles.
# - Strong track record in scholarly research with H-index of `32` and total citation of 3200+.
# ''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Sanchit Goel</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# space, time, space = st.columns([0.2,8,0.2])
# with time:
#   st.markdown('## &nbsp &nbsp &nbsp &nbsp  My Data science journey', unsafe_allow_html=True)
#   # load data


#   with open('example.json', "r") as f:
#       data = f.read()

#   # render timeline
#   timeline(data, height=500)
#####################
# Custom function for printing text
def txt(a, b):
  space, col1, col2 = st.columns([0.1,4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  space, col1, col2 = st.columns([0.5,1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  space, col1, col2 = st.columns([0.5,1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  space, col1, col2, col3 = st.columns([0.15,0.8,3.5,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################

st.markdown('''
## Education
''')

txt('**Post Graduate Diploma (Computer Science)**,&nbsp *Ashoka University*, India',
'2019-2020')
space, text = st.columns([0,8])
with text:
  st.markdown('''
  -&nbspMinors in Computer Science, GPA: `3.6`
  -&nbsp Deans List`
  \n
  -&nbspRelevant Courses : 
  \n Computer Sceince: &nbsp Advanced Machine Learning, Advanced Programing,  Algorithms, Data Mining and Warehousing
  \n Maths: &nbsp Linear Algebra, Calculus, Statistical Inference
  ''', unsafe_allow_html = True)

st.write("##")

txt('**Bachelors of Arts (Economics)**,&nbsp *Ashoka University*, India',
'2016-2019')
space, text = st.columns([0.5,8])
with text:
  st.markdown('''
  -&nbspEconmics Major, GPA: `3.3`
  \n
  -&nbspRelevant Courses : 
  \n &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Economics: &nbsp Advanced Econometrics, Statistics for Economics, Networks crowds and Internet, Game Theory
  \n &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Finance: &nbsp Advanced Financial Management, 
  \n &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Computer Science: &nbsp Introduction to Programing

  ''', unsafe_allow_html = True)

#####################
st.markdown('''
## Work Experience
''')

txt('**NLP Engineer**, Fractal Analytics',
'Oct 2020-Present')
space, text, space = st.columns([0.5,8,2])
with text:
  st.markdown('''
  -Developed an intelligent automation tool that automates the processing of insurance claims (PA and FWA) for US health insurance firms. Solution digitizes and extracts relevant details from the insurance forms using Natural Language Processing (NLP) models/libraries like Spacy, PYSBD, and Regex, and applies validation rules to check if the claim is valid.
  \n-Worked on developing an automated Invoice processing solution using Image OCR and Natural lan- guage processing. Trained a text classifier to identify relevant segments of an invoice. Used NLP to extract required information using pattern matching.
  ''')

st.write("##")
txt('**Research Assistant**, Dr. Ashwini Deshpande',
'Aug - Sept 2021')
space, text, space = st.columns([0.5,8,2])
with text:
  st.markdown('''
  Worked with Dr. Ashwini Pande and Dr. Joshua Merfeld on the paper ‘Decentralization and Program Implementation’ to study the impact of district splits on the effectiveness of Program implementation. I prepared the dataset of over 800 districts and 7000 blocks using web scraping and census datasets. I identified district splits in India from 2011-20 by mapping block level changes in a district year over year, allowing us to study how district splits affected NREGA implementation in India from 2010-20.
  ''')
  
st.write("##")
txt('**Research Assistant**, Dr. Kanika Mahajan',
'May - July 2020')
space, text, space = st.columns([0.5,8,2])
with text:
  st.markdown('''
  -Worked on the now published journal ‘Covid 19 and Supply chain disruption’. I was responsible for cleaning the data and calculating the distances between production zones and retail centres by using google maps API to find the impact of distance on supply chain disruptions.
  \n-Worked on the paper ‘Words matter: Gender, Jobs and Applicant Behaviour’, to examine how implicit gender preference in Job ads leads to differential labor market out- comes. I used NLP techniques like tf-idf, topic modeling and word clouds to understand the difference between the kind of jobs offered and the keywords associated with respective gender preferred jobs.
  ''')

st.write("##")
txt('**Business Analyst Intern**, National Skill Foundation of India',
'June - July 2017')
space, text, space = st.columns([0.5,8,2])
with text:
  st.markdown('''
  Went to Jharkhand to study the Lac industry. Surveyed over 30 farmers and created a micro business plan for improving current NSFI’s college curriculum on growing LAC.
  ''')

twitterazi_file = open('media/Twitterazi_demo_2.mp4', 'rb')
twitterazi_bytes = twitterazi_file.read()

stocksnapshot_file = open('media/Stock_snapshot_demo.mp4', 'rb')
stocksnapshot_bytes = stocksnapshot_file.read()

bookspine_file = open('media/Book_spine_demo.mp4', 'rb')
bookspine_bytes = bookspine_file.read()
#####################
st.markdown('''
## Projects
''')
txt4('**Book Spine Detection**', 'Developed an app for a client that segregates and digitizes the books in a book shelf\'s image. Uses canny edge detection method to detect edges in a photo and then applies hough transformation to identify book spine edges. Then the image is cropped on the identified edges and digitized to get the text on spine.', 'none')
space, exp, space = st.columns([1,3.8,1.1])
with exp:
  with st.expander("See Demo"):
    st.video(bookspine_bytes)

txt4('**Twitterazi**', 'A web app that finds the topics a twitter user has tweeted about in the past month. It accurately recognises people, organisations, locations and keywords in the tweets using Spacy and Regex, which can then be used to filter out tweets containing that entity.', '[Link](https://sanchitgoel7-twitterazi-app-ntuijm.streamlitapp.com/)')
space, exp, space = st.columns([1,3.8,1.1])
with exp:
  with st.expander("See Demo"):
    st.video(twitterazi_bytes)

txt4('**Stocksnapshot**', 'Developed a one-stop stock analysis tool that gives a financial overview of a company by scraping over 20yr+ financial data. The App also has a built in DCF calculator for a quick Intrinsic value calculation of a stock.', '[Link](https://stocksnapshot.herokuapp.com/) &nbsp &nbsp [Github](https://stocksnapshot.herokuapp.com/)')

space, vid, space = st.columns([1,3.8,1.1])
with vid:
  with st.expander("See Demo"):
    st.video(stocksnapshot_bytes)

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `SQL`,`Java`')
txt3('Natural Language Processing','`Spacy`,`NLTK`,`PYSBD`,`TF-DF`,`LDA`')
txt3('Data visualization', '`PowerBi`,`Tableau`,`matplotlib`, `seaborn`, `altair`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`streamlit`, `CSS`')
txt3('Model deployment', '`streamlit`,`Heroku`, `AWS`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/chanin-nantasenamat')
txt2('Twitter', 'https://twitter.com/thedataprof')
txt2('GitHub', 'https://github.com/chaninn/')

