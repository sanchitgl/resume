import streamlit as st
from PIL import Image

image = Image.open('media/resume_logo.png')

st.set_page_config(page_title="Sanchit Goel", page_icon = image)
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
#####################
# Header 

# def set_width(width: str):
#   st.markdown(
#   f"""
#   .appview-container.main.block-container{{max-width:{width};}}
#   """,
#       unsafe_allow_html=True,
#   )


# set_width("300px")

st.markdown(
        f"""
<style>
    .appview-container .main .block-container{{
        max-width: {1300}px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )

#hide image fullscreen icon
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''
st.markdown(hide_img_fs, unsafe_allow_html=True)

#hide copy link icon on text
st.markdown("""
        <style>
        .css-eczf16 {display: none}
        </style>
        """, unsafe_allow_html=True)


st.write('''
# Hi! I'm Sanchit Goel 
''')
space, im, desc, space = st.columns([1.5,1,3,1.5])
with im:
  image = Image.open('media/dp.jpg')
  st.image(image, width=150)
with desc:
  st.write('''I am currently a data scientist at Fractal.ai, developing intelligent solutions for fortune 500 clients. **Research Interests** : Applications of NLP and AI/ML in the health care and social sciences space. \n\nApart from that, I am also a keen follower of Formula 1, and love to play guitar in my free time :) ''')
  st.markdown('[Github](https://github.com/sanchitgl) &nbsp; [LinkedIn](https://www.linkedin.com/in/-sanchitgoel) &nbsp; [Resume](https://drive.google.com/file/d/1hiR6aSMxQiL7N1GhbZzEAcx4X0-jGgv_/view?usp=sharing)') 

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
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt5(a):
    st.markdown(a)

def txt(a, b):
  space, col1, col2, space = st.columns([2,4,1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)


################
space, text, space = st.columns([2,5,2])
with text:
  st.markdown('''
  ## Work Experience
  ''')

txt('**Data Scientist**, [**Fractal.ai**](https://fractal.ai/)',
'Oct 2020-Present')

space, text, space = st.columns([2,5,2])
with text:
  st.markdown('''
  - **Digital Analytics**:  Currently working with Merck- Studying their consumer interaction data to improve their marketing campaigns' effectiveness. 
  - **Propay.bot**: An intelligent solution that processes and verifies health insurance claims (PA and FWA contracts) using NLP models - Spacy, PYSBD and Regex. **Impact**- In process of adoption by top health insurance firms - United Health & Cigna.
  - **Power BI chatbot**: A POC for Heinekin, allowing upper management to directly query their BI dashboard natural language. Used Azure Bot Service. **Impact**- POC was accepted by Heineken and project will be financed later this year.
  - **Invoice Information Extraction**: An E2E solution that streamlines and automates Invoice processing - from Information extraction to client's ERP update. Using Google Vision OCR and NLP (LSTM, Regex). **Impact**- Saved 100+ hrs in Labor monthly and avoided manual errors.
    ''')


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
hand_gesture_img = Image.open('media/hand_gest.png')
obfuscate_img = Image.open('media/Image_obfuscations.png')

#####################
st.write("&nbsp;")
st.markdown('''
# Past Projects
''')

st.markdown("""
<style>
.small-font {
    font-size:14px !important;
}
.med-font {
    font-size:16px !important;
}
</style>
""", unsafe_allow_html=True)

def small_text(head, str, skills):
  st.markdown('''<b class='med-font'>'''+head+'''</b><p class='small-font'>'''+str+'''  
  **Skills:**'''+skills+"</p>", unsafe_allow_html=True)
  #st.markdown("<p class='small-font'>Skills:"+skills+"</p>", unsafe_allow_html=True)

def load_twitterazi():
  st.video(twitterazi_bytes)
  #st.image(book_spine_img, use_column_width ="always")
  small_text("[Twitterazzi](https://sanchitgoel7-twitterazi-app-ntuijm.streamlitapp.com/)", ''' Web app that gives a quick overview of an influencer's twitter activity. It accurately identifies keywords, entities (Person, organizations & locations) 
  and sentiment by processing user's recent tweets.'''," POS tagging, NER, Wordcloud, Regex")

def load_bookspine():
  st.video(bookspine_bytes)
  #st.image(book_spine_img, use_column_width ="always")
  small_text("Book Shelf Digitization", '''Web app that recognizes books in a book shelf image. Sements images by 
  identifying book spines using canny edge detection and Hough transformation. Then digitizes and extracts the text from the segmented images to identify books.''',
  " Canny Edge Detection, Hough Transformation, Google Vision API")


def load_imageobf():
  st.image(obfuscate_img, width = 320)
  small_text("Reconstruction of Obfuscated Images", '''Trained Convolutional Autoencoders on 13000 images to fix 3 types of Obfuscations(blur, pixelation and speckle noise in facial images.'''
  ," Autoecncoders")


def load_hand_reco():
  st.image(hand_gesture_img,  width = 340)
  small_text("Hand Gesture Recognition",'''Trained a convolutional neural network(CNN) to recognize hand gestures. We used VPLU dataset of 1100 images to train the classifier, the model was able to correctly 
  classify hand gestures into 11 classes with ∼ 98% accuracy.'''," CNN")

def load_stock_snap():
  st.video(stocksnapshot_bytes)
  small_text("Stocksnapshot",'''Developed a stock analysis web app that scrapes over 20 yr+ financial data - over 100 monthly active users. 
  Also has a built in DCF calculator for a quick Intrinsic value calculation of a stock. Hosted the app on Heroku.'''," Web scraping, Regex, ALtair charts, Streamlit")

space, wid, space = st.columns([3.5,4,2])
with wid:
  type_projects = st.radio("project type", ("All","NLP", "Image-Processing", "ML"), horizontal=True, label_visibility = 'collapsed')
  
if type_projects == "All":
  space, p1, space, p2,space, p3, space = st.columns([0.4,2,0.05,2,0.05,2,0.4])
  with p1:
    load_bookspine()
    #st.image(book_spine_img, use_column_width ="always")
    #st.markdown('<p class="small-font">Developed an app for a client that segregates and digitizes the books in a book shelf\'s image. Uses canny edge detection method to detect edges in a photo and then applies hough transformation to identify book spine edges. Then the image is cropped on the identified edges and digitized to get the text on spine.</p>', unsafe_allow_html=True)
    # with st.expander("See Demo"):
    #   st.video(bookspine_bytes)


  #st.markdown("""---""")
  with p2:
    load_twitterazi()
    #txt4('**Twitterazi**', 'A web app that finds the topics a twitter user has tweeted about in the past month. It accurately recognises people, organisations, locations and keywords in the tweets using Spacy and Regex, which can then be used to filter out tweets containing that entity.', '[Link](https://sanchitgoel7-twitterazi-app-ntuijm.streamlitapp.com/)')

  with p3:
    load_imageobf()
    #txt4('**Reconstruction of Obfuscated Images**','Used Convolutional Autoencoders to fix 3 types of Obfuscations(blur, pixelation and speckle noise) in facial images. We trained 3 different Autencoders on about 13000 images to handle the different types of obfuscations', '[PDF](https://drive.google.com/file/d/1ac9nbv1E7MKduiapijJC-A8mCk1n9XAZ/view?usp=sharing)')
  
  st.markdown("""---""")
  space, p1, space, p2,space, p3, space = st.columns([0.4,2,0.05,2,0.05,2,0.4])
  with p1:
    load_hand_reco()
    #txt4('**Hand Gesture Recognition**', 'Trained a convolutional neural network(CNN) to recognize hand gestures. We used VPLU dataset of 1100 images to train the classifier, the model was able to correctly classify hand gestures into 11 classes with ∼ 98% accuracy.', '[PDF](https://drive.google.com/file/d/1tb3uY4i6B9PloM7Pl08O8VBR4N9WbS5E/view?usp=sharing)')
  #st.markdown("""---""")

  with p2:
    load_stock_snap()
    #txt4('**Stocksnapshot**', 'Developed a one-stop stock analysis tool that gives a financial overview of a company by scraping over 20yr+ financial data. The App also has a built in DCF calculator for a quick Intrinsic value calculation of a stock.', '[Link](https://stocksnapshot.herokuapp.com/) &nbsp &nbsp [Github](https://stocksnapshot.herokuapp.com/)')


elif type_projects == "NLP":
  space, p1, space, p2,space, p3, space = st.columns([0.4,2,0.05,2,0.05,2,0.4])
  with p1:
    load_twitterazi()

  with p2:
    load_stock_snap()

elif type_projects == "Image-Processing":
  space, p1, space, p2,space, p3, space = st.columns([0.4,2,0.05,2,0.05,2,0.4])
  with p1:
    load_bookspine()
  with p2:
    load_imageobf()
  with p3:
    load_hand_reco()

elif type_projects == "ML":
  space, p1, space, p2,space, p3, space = st.columns([0.4,2,0.05,2,0.05,2,0.4])
  with p1:
    load_imageobf()
  with p2:
    load_hand_reco()
  
#####################
# st.markdown('''
# ## Skills
# ''')
# txt3('Programming', '`Python`, `SQL`,`Java`')
# txt3('Natural Language Processing','`Spacy`,`NLTK`,`PYSBD`,`TF-DF`,`LDA`')
# txt3('Data visualization', '`PowerBi`,`Tableau`,`matplotlib`, `seaborn`, `altair`')
# txt3('Machine Learning', '`scikit-learn`,`TensorFlow`')
# txt3('User Interface', '`streamlit`, `CSS`')
# txt3('Model deployment', '`streamlit`,`Heroku`, `AWS`, `Azure`')



