import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
#####################
# Header 
st.write('''
# Hi! I'm Sanchit Goel 
''')
im, desc = st.columns([1,3])
with im:
    image = Image.open('media/dp.jpg')
    st.image(image, width=150)
with desc:
    st.write("I am currently a data scientist at Fractal.ai, and interested in research relating to applications of NLP and AI/ML in the health care and social sciences space.")

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/-sanchitgoel" target="_blank">Sanchit Goel</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
        <li class="nav-item">
        <a class="nav-link" href="#research">Research</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#past-projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt5(a):
    st.markdown(a)


def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.3,3.9,0.25])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

def txt6(a, img,  b, c):
  col1, col2, col3 = st.columns([1.3,3.9,0.25])
  with col1:
    #st.markdown(a)
    st.image(img, use_column_width ="always")
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

################
st.markdown('''
## Work Experience
''')

txt('**Data Scientist**, [**Fractal.ai**](https://fractal.ai/)',
'Oct 2020-Present')
st.markdown('''
  -Developed an intelligent automation tool that automates the processing of insurance claims (PA and FWA) for US health insurance firms. Solution digitizes and extracts relevant details from the insurance forms using Natural Language Processing (NLP) models/libraries like Spacy, PYSBD, and Regex, and applies validation rules to check if the claim is valid.
  \n-Worked on developing an automated Invoice processing solution using Image OCR and Natural lan- guage processing. Trained a text classifier to identify relevant segments of an invoice. Used NLP to extract required information using pattern matching.
  ''')

#####################
# st.markdown('''
# ## Education
# ''')

# txt('**Post Graduate Diploma (Computer Science)**,&nbsp *Ashoka University*, India',
# '2019-2020')
# st.markdown('''
#   &nbspMinors in Computer Science, GPA: `3.6`, &nbsp Dean's List
#   ''', unsafe_allow_html = True)

# txt('**Bachelors of Arts (Economics)**,&nbsp *Ashoka University*, India',
# '2016-2019')
# st.markdown('''
# &nbspMajors in Economics, GPA: `3.4`
# ''')
# st.write("##")
#####################
st.markdown('''
## Research
''')

# txt('**NLP Engineer**, Fractal Analytics',
# 'Oct 2020-Present')
# st.markdown('''
#   -Developed an intelligent automation tool that automates the processing of insurance claims (PA and FWA) for US health insurance firms. Solution digitizes and extracts relevant details from the insurance forms using Natural Language Processing (NLP) models/libraries like Spacy, PYSBD, and Regex, and applies validation rules to check if the claim is valid.
#   \n-Worked on developing an automated Invoice processing solution using Image OCR and Natural lan- guage processing. Trained a text classifier to identify relevant segments of an invoice. Used NLP to extract required information using pattern matching.
#   ''')

#st.write("##")
txt5('**Decentralization and Program Implementation**  - Research Assistant,  [Dr. Ashwini Deshpande](https://scholar.google.com/citations?user=gH37QQkAAAAJ&hl=en)')
st.markdown('''
  Worked as a research assistant on the working paper ‘Decentralization and Program Implementation’ to study the impact of district splits on the effectiveness of Program implementation. I prepared the dataset of over 800 districts and 7000 blocks using web scraping and census datasets. I identified district splits in India from 2011-20 by mapping block level changes in a district year over year, allowing us to study how district splits affected NREGA implementation in India from 2010-20.
  ''')

st.markdown("""---""")
txt5('[**Words matter: Gender, Jobs and Applicant Behaviour \[IZA\]**](https://docs.iza.org/dp14497.pdf) - Research Assistant,  [Dr. Kanika Mahajan](https://sites.google.com/view/kanikamahajan/home?authuser=0)')
st.markdown('''
  Worked as a research assistant on the paper ‘Words matter: Gender, Jobs and Applicant Behaviour’, to examine how implicit gender preference in Job ads leads to differential labor market out- comes. I used NLP techniques like tf-idf, topic modeling and word clouds to understand the difference between the kind of jobs offered and the keywords associated with respective gender preferred jobs.
  ''')

st.markdown("""---""")
txt5('**[Covid 19 and Supply chain disruption \[AAEA\]](https://onlinelibrary.wiley.com/doi/full/10.1111/ajae.12158)** - Research Assistant,  [Dr. Kanika Mahajan](https://sites.google.com/view/kanikamahajan/home?authuser=0)')
st.markdown('''
  Worked on the now published journal ‘Covid 19 and Supply chain disruption’. I was responsible for cleaning the data and calculating the distances between production zones and retail centres by using google maps API to find the impact of distance on supply chain disruptions.
  ''')

st.markdown("""---""")
txt5('**[Auto Mobile Slowdown: A Qunatitative Study](https://drive.google.com/file/d/1hq8DhX0UYkx2-82XsmB1sxAa39emTvap/view?usp=sharing)** - Indpendent Study Module, [Dr. Debayan Gupta](https://debayangupta.com/work.htm)')
st.markdown('''
  Studied the role factors like regulation changes, NBFC crisis, rise in ride hailing services and consumer confidence played on bringing about the Automobile slowdown in 2019. Used OLS estimation to find the impact of mentioned factors.
  ''')


# st.write("##")
# txt('**Business Analyst Intern**, National Skill Foundation of India',
# 'June - July 2017')
# st.markdown('''
#   Went to Jharkhand to study the Lac industry. Surveyed over 30 farmers and created a micro business plan for improving current NSFI’s college curriculum on growing LAC.
#   ''')

#####################

twitterazi_file = open('media/Twitterazi_demo_2.mp4', 'rb')
twitterazi_bytes = twitterazi_file.read()

stocksnapshot_file = open('media/Stock_snapshot_demo.mp4', 'rb')
stocksnapshot_bytes = stocksnapshot_file.read()

bookspine_file = open('media/Book_spine_demo.mp4', 'rb')
bookspine_bytes = bookspine_file.read()

book_spine_img = Image.open('media/Book_spin_detec.png')
#####################
st.write("&nbsp;")
st.markdown('''
## Past Projects
''')
txt6('**Book Spine Detection**', book_spine_img, 'Developed an app for a client that segregates and digitizes the books in a book shelf\'s image. Uses canny edge detection method to detect edges in a photo and then applies hough transformation to identify book spine edges. Then the image is cropped on the identified edges and digitized to get the text on spine.', 'none')
space, exp, space = st.columns([1.3,3.9,0.25])
with exp:
  with st.expander("See Demo"):
    st.video(bookspine_bytes)
st.markdown("""---""")
txt4('**Twitterazi**', 'A web app that finds the topics a twitter user has tweeted about in the past month. It accurately recognises people, organisations, locations and keywords in the tweets using Spacy and Regex, which can then be used to filter out tweets containing that entity.', '[Link](https://sanchitgoel7-twitterazi-app-ntuijm.streamlitapp.com/)')
space, exp, space = st.columns([1.3,3.9,0.25])
with exp:
  with st.expander("See Demo"):
    st.video(twitterazi_bytes)
st.markdown("""---""")

txt4('**Reconstruction of Obfuscated Images**','Used Convolutional Autoencoders to fix 3 types of Obfuscations(blur, pixelation and speckle noise) in facial images. We trained 3 different Autencoders on about 13000 images to handle the different types of obfuscations', '[PDF](https://drive.google.com/file/d/1ac9nbv1E7MKduiapijJC-A8mCk1n9XAZ/view?usp=sharing)')
st.markdown("""---""")
txt4('**Hand Gesture Recognition**', 'Trained a convolutional neural network(CNN) to recognize hand gestures. We used VPLU dataset of 1100 images to train the classifier, the model was able to correctly classify hand gestures into 11 classes with ∼ 98% accuracy.', '[PDF](https://drive.google.com/file/d/1tb3uY4i6B9PloM7Pl08O8VBR4N9WbS5E/view?usp=sharing)')
st.markdown("""---""")
txt4('**Stocksnapshot**', 'Developed a one-stop stock analysis tool that gives a financial overview of a company by scraping over 20yr+ financial data. The App also has a built in DCF calculator for a quick Intrinsic value calculation of a stock.', '[Link](https://stocksnapshot.herokuapp.com/) &nbsp &nbsp [Github](https://stocksnapshot.herokuapp.com/)')
space, vid, space = st.columns([1.3,3.9,0.25])
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
txt3('Machine Learning', '`scikit-learn`,`TensorFlow`')
txt3('User Interface', '`streamlit`, `CSS`')
txt3('Model deployment', '`streamlit`,`Heroku`, `AWS`, `Azure`')



