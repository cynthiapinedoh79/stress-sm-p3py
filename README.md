![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
# 📊 Project3 pyhton – stress-sm-p3py

## Code Institute - Second Milestone Project: User-Centric Frontend Development
![GitHub repo size](https://img.shields.io/github/repo-size/cynthiapinedoh79/stress-sm-p3py)
![GitHub last commit](https://img.shields.io/github/last-commit/cynthiapinedoh79/stress-sm-p3py)
[![View Demo](https://img.shields.io/badge/View-Demo-brightgreen)](https://cynthiapinedoh79.github.io/stress-sm-p3py/)

![HTML](https://img.shields.io/badge/HTML5-0%25-%23E34F26?style=flat&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-0%25-%231572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-0%25-%23F7DF1E?style=flat&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-100%25-3776AB?style=flat&logo=python&logoColor=white)
![Dockerfile](https://img.shields.io/badge/Dockerfile-0%25-384d54?style=flat)




## 🔗 Live Demo  
<!-- [👉 Try the live website](https://cynthiapinedoh79.github.io/stress-sm-p3py/) -->
[👉 Try it live on Heroku](https://stress-sm-p3py-6b1a0e94ecd6.herokuapp.com/)

<!-- [Main Screenshots](assets/images/readme/amIR/AIR-Home.png) -->

---

Stress-sm-p3py is a python code deployed in heroku.

# 📋 Table of Contents
- [🧾 Project Overview](#🧾-project-overview)
<!--
- [📱 Am I Responsive? - Demo](#📱-am-i-responsive---demo)
-->
- [🎯 UX](#🎯-ux)
- [🧑‍💼 User Stories](#🧑‍💼-user-stories)
- [🎨 Design Choices](#🎨-design-choices)
<!--
- [📐 Five Planes UXD](#📐-five-planes-uxd)
  - [📌 Strategy](#📌-strategy)
  - [📐 Scope](#📐-scope)
  - [🏗️ Structure](#🏗️-structure)
  - [🦴 Skeleton](#🦴-skeleton)
  - [🎨 Surface](#🎨-surface)
-->
- [🛠️ Technologies & Design Choices](#🛠️-technologies--design-choices)
- [✨ Features](#✨-features)
  - [🚀 Existing Features](#🚀-existing-features)
  - [🔮 Features Left to Implement](#🔮-features-left-to-implement)
  - [🧑‍💻 Languages Used](#🧑‍💻-languages-used)
  - [🧰 Frameworks, Libraries & Programs Used](#🧰-frameworks-libraries--programs-used)
- [🧪 Testing & Validation](#🧪-testing--validation)
  - [✅ Browser & Device Testing](#✅-browser--device-testing)
  - [✅ Validator Testing](#✅-validator-testing)
  - [✅ Accessibility Testing](#✅-accessibility-testing)
  - [✅ Console in Google Chrome DevTools-"Inspect" Testing](#✅-console-in-google-chrome-devtools-inspect-testing)
  - [🧑‍💻 Testing User Stories – User Experience (UX) Evaluation](#🧑‍💻-testing-user-stories--user-experience-ux-evaluation)

  - [🐞 Bugs](#🐞-bugs)
  - [📥 Deployment](#📥-deployment)
  - [🌐 GitHub Pages Deployment](#🌐-github-pages-deployment)
  - [🍴 Forking the GitHub Repository](#🍴-forking-the-github-repository)
  - [📂 Making a Local Clone](#📂-making-a-local-clone)
- [🙏 Credits & Acknowledgements](#🙏-credits--acknowledgements)

---

## 🧾 Project Overview
stress-sm-p3py is a terminal-based survey to measure digital fatigue and stress.

---

<!--
## 📱 Am I Responsive? - Demo
All pages were designed with **Responsive Design** to provide a consistent experience across various screen sizes and devices.

![Responsive devices -Home](assets/images/readme/amIR/AIR-Home.png)
-->

### A live demo to the website 
[👉 Try the live website](https://cynthiapinedoh79.github.io/stress-sm-p3py/) 

---

## 🎯 UX
### Target Audience:
1. Professionals and remote workers – people experiencing screen fatigue or tech overload.
2. Students and digital natives – who use social media and games heavily.
3. Mental health coaches or digital wellness advocates – interested in simple tools for tracking digital habits.

### Core UX Goals:
<!--
1. Build trust and credibility through clean design and intuitive structure
2. Offer quick, interactive content that’s informative yet fun
3. Provide actionable takeaways (e.g., IRS form, consultation link)
4. Ensure accessibility and responsive design for all devices
5. Create opportunities for return visits and deeper engagement
-->
1. Build trust and clarity through a guided, conversational CLI experience
Use clear prompts, validation feedback, and a welcoming tone to help users feel comfortable sharing personal info.
2. Deliver fast, interactive feedback based on user input
Instantly return personalized and group-based recommendations to reinforce user engagement and learning.
3. Make results actionable and motivating
Encourage digital wellness with tailored advice (e.g., “Try screen breaks,” “Do offline hobbies”) that users can immediately apply.
4. Design for inclusivity and accessibility in text-based environments
Keep questions simple, jargon-free, and keyboard-navigable for all reading levels and users, including non-native English speakers.
5. Create potential for future growth (e.g., web app, gamification, dashboards)
Lay the groundwork for expanding into more dynamic formats or professional use (e.g., coaches, teachers).

### Main Site Goals:
<!--
- Promote core services through engaging features
- Attract potential clients through playful, educational content
- Help users assess their bookkeeping needs via a quick quiz
- Provide added value—discounts, tools, and practical insights—even for casual visitors
- Offer a ready-to-fill IRS Form 1040 PDF as part of the service suite
- (Coming Soon) Introduce a Tax Comparison Tool to highlight potential savings between LLC and S-Corp business structures
- (Coming Soon) Launch a Match Game that delivers quick, actionable tips for smarter financial decisions—covering bookkeeping, taxes, and business planning in a fun, easy-to-understand format
-->

- Promote digital wellness by helping users understand the impact of screen time, social media, and tech fatigue on their stress levels
- Offer instant, personalized and group recommendations based on individual habits and emotional feedback
- Encourage self-reflection through a short, engaging survey with zero judgment and simple language
- Present group-level comparisons to help users see how their habits align with or differ from peers
- Securely store all data in Google Sheets, enabling future analysis, usage tracking, or reporting
- (Coming Soon) Build a simple web-based version for broader accessibility and visual enhancements
- (Coming Soon) Add a “Stress Tracker” dashboard that visualizes personal trends over time and recommends habit adjustments

---


## 🧑‍💼 User Stories
- My Goal as Developer:
  As the sole developer of this Python-based app, my mission is to create a smooth, insightful, and interactive experience that helps users better understand how digital habits affect their stress levels. The tool should feel helpful, safe, and informative — encouraging users to reflect on their digital well-being and take actionable steps to improve it.
<!--
As the sole developer of this website, my mission is to provide you with an enjoyable and user-friendly experience while delivering clear, concise, and accurate information about our services — sparking your interest in what we offer.
-->

- User Experience Objectives:
From the user's perspective, this app is designed with the following key goals:
  - I want to complete the survey quickly and clearly without confusion.
  - I need the instructions and questions to be easy to understand and answer.
  - I appreciate seeing my results visually and getting meaningful feedback right away.
  - I want to feel that my answers are confidential and respected.
  - I should be able to revisit and see my progress (optional for future enhancement).

<!-->
  - I want to navigate this website quickly and easily.
  - I should be able to use a mouse, keyboard, or touchscreen effortlessly.
  - I value high-quality, well-organized information that I can consume in just a few minutes.
  - As a user, I need a simple and clear way to get in touch with you.
-->

  ### First-Time Visitor Goals

  - As a first-time user:
      1. I want to understand what this survey is about and how it will help me.
      2. I’d like to complete the survey in under 5–10 minutes.
      3. I want to receive personalized feedback or recommendations based on my answers.
      4. I want reassurance that my data is treated respectfully and securely.

<!--
      1. To quickly understand the main purpose of the site and discover what your company offers.
      2. To navigate the site effortlessly and find content that captures my interest.
      3. To be visually engaged by an attractive and inviting website that encourages me to explore further.
      4. To easily locate your contact information — ideally supported by testimonials or customer reviews to build trust.
-->

  ### Returning Visitor Goals
 
  - As a returning user:
      1. I want to take the survey again and compare results over time (if available).
      2. I’d like to see insights based on other users’ averages vs. mine.
      3. I may want to receive a summary of my responses and tips.

  <!--
       1. To find more detailed information about the services provided, including working hours.
       2. To easily discover the best way to contact the organization for any questions or support.
       3. To understand the available methods of communication — whether through Zoom, Skype, phone, or in-person meetings.
  -->

  ### Frequent User Goals

  - As a frequent user:
      1. I want to track my digital stress patterns and improvements.
      2. I want visual summaries (e.g., bar charts) comparing my screen time, app usage, and stress over time.
      3. I want to explore wellness tips, exercises, or links to mindfulness apps for support.

  <!--
       1. To conveniently access and fill out IRS Form 1040 directly through the site.
       2. To view brief and clear comparisons — such as LLC vs. S-Corp — to help make informed decisions.
  -->

---

## 🎨 Design Choices
  ### Description
  This command-line Python app is thoughtfully designed to guide users through a quick and insightful survey that explores the relationship between digital habits and stress levels. While the interface is minimal, the user experience is intentionally structured to feel conversational, supportive, and meaningful. The goal is not only to collect data, but to help users reflect and take action on their digital wellness.

  #### Key Design Principles
  1. User-Centered Flow:
     The questions follow a logical and empathetic order — starting with basic habits and gently leading into emotional well-being — ensuring users never feel overwhelmed or judged.

  2. Clarity & Simplicity:
     Instructions and questions are short, jargon-free, and formatted with consistent spacing for readability in the terminal.

  3. Immediate Feedback:
     Upon completion, users receive personalized summaries, visual graphs (via Matplotlib), and practical recommendations based on their responses.

  4. Purposeful Interactivity:
     Users engage in a step-by-step format that feels natural and smooth, including options to skip non-relevant sections and retry invalid inputs without frustration.

  5. Visual & Analytical Layer:
     While text-based in interaction, the app enhances insights with bar graphs that compare the user’s habits to average data from others — making results feel more relevant and motivating.

  6. Trust & Privacy Focus:
     The app communicates clearly that responses are stored securely in Google Sheets (with no personal identifiers), reinforcing user confidence in sharing honest answers.

<!--
  This website is designed for visitors and new customers to explore, learn, win rewards, and enjoy an engaging experience while navigating through different pages.
-->

<!--
  ### Typography
  Inter, Roboto family font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Roboto is a clean font used frequently in programming, so it is both attractive and appropriate.

### Color Palette 
  - **Fonts:** Roboto, Inter – clean and modern  
  - **Colors:**  
    - Purple: trust and creativity  
    - Red/Orange: urgency and emphasis  
    - Muted tones: professionalism  
  - [Contrast checked with WebAIM](https://webaim.org/resources/contrastchecker/)

  ### Colour Psychology
  ![Colour Psicology](assets/images/readme/PsColor.png)
  ![Contrast checked with WebAIM](assets/images/readme/PsColor1.png)

  ### Imagery  
  Clear and attractive images support the theme and maintain strong contrast with text for optimal readability.
- Financial and office-themed backgrounds  
- High contrast text overlays for readability

---


  ### 1. Home: index.html
        
  - Background: 
  A blurred photo of financial charts and a blue pen (soft blue, red, beige tones)

  - Text: Dark purple for "Needs Bookkeeping?"
  - Buttons: Quick Quiz, Check this! and Play & Save!
    - Background Color: Purple.
    - Hover: Dark Red.
  - Color Mood: Professional, calm, and trustworthy (purple conveys reliability and creativity).

-->


## 📐 Five planes UXD

### 📌 Strategy
The goal of this project is to help users evaluate their digital stress levels and receive personalized recommendations. The app is built with clarity, ease of use, and meaningful feedback at its core—making it both functional and insightful.

<!--
![Strategy](assets/images/readme/fivePlanes/strategy.png)
-->

### 📐 Scope
The application targets two key audiences:

First-time users: 
Can complete a quick survey, receive immediate results and feedback, and explore wellness tips or trends based on their responses.

Returning users: 
Can compare past entries, observe trends in their digital habits, and access actionable suggestions for reducing digital fatigue or improving well-being.

Key features include:

- Digital stress survey
- Personalized recommendations
- Automatic chart generation from user data
- Optional comparison with previous scores
- View summaries via Google Sheets integration

<!--
The site is designed for two main user groups:
1.	Visitors, who can enjoy interactive games, helpful tips, new information, and practical advice.
2.	Potential new customers, who can explore special offers like a bookkeeping bonus award, contact us easily, or quickly access the Form 1040 submission link.

![Scope pg1](assets/images/readme/fivePlanes/scope1.png)

![Scope pg2](assets/images/readme/fivePlanes/scope2.png)
-->

### 🏗️ Structure
The structure of the application was planned around a smooth, user-friendly experience via the terminal (CLI), with potential to scale into a web app.

Core Functional Areas:

1. Welcome Section – Brief introduction and user prompt
2. Survey – 8+ questions covering screen time, emotional states, fatigue, exercise, etc.
3. Result Calculation – Based on weighted input
4. Feedback & Tips – Tailored results with stress-reduction suggestions
5. Data Logging – Responses stored in Google Sheets
6. Graph Output – Visual insight into digital stress using Matplotlib

<!--
The website is designed with HTML5, CSS3 and JS.

**Website Pages:**
1. **_Needs Bookkepping?:_** Main page with three buttons (Quiz, Check This! and Play & Save!)
2. **_Quiz:_** A brief quiz with a few questions that are scored to assess user needs.
3. **_Feedback:_** A feedback message is shown if your answers indicate that you may need our help or services. It includes a link to fill out Form 1040 and a direct link to contact us through our website.
4. **_CheckThis:_** Displays Bookkeeping Fact Cards with useful information.
6. **_Prize:_** Try Your Luck! Win a special prize or bookkeeping bonus—just reach out to claim your reward!

![Structure](assets/images/readme/fivePlanes/structure.png)
-->

### 🦴 Skeleton
The system logic follows a clear, linear flow, with decision-making trees and structured question routing based on user inputs. Error handling ensures data integrity, and repeated use is encouraged by storing timestamps and results for future comparisons.

Planned Enhancements:
- Add progress tracking
- Option to download a PDF summary
- Provide external links to resources like mindfulness apps or articles

<!--
The website is designed to be clear and simple. And the site has a simple tree structure with hierarchical flows from top to bottom.
-->

<!--
**Wireframe**
The wireframe is designed using Balsamiq software 
[Balsamic](https://balsamiq.cloud/ss26tqg/p4441iq/rD01A)

#### Home
![Home](assets/images/readme/Bals/Bals-Home.png)
-->

### 🎨 Surface
The CLI interface is designed for simplicity and clarity using structured prompts, progress indicators, and color-coded feedback (where supported). If expanded into a GUI, a soft palette of calming blues and greens would be used to reflect wellness, balance, and trust.

<!--
To create a pleasing and understandable view, I opt for natural colors such as earth, green, and a range of tones that complement and contrast each other.
-->
---

## 🛠️ Technologies & Design Choices
1. **Python** – The core programming language used to build the digital stress survey, manage logic, handle user input, and communicate with external APIs.
2. **gspread & Google Sheets API** – Enables secure storage of user responses in a connected Google Sheet, allowing for data logging, analysis, and comparisons over time.
3. **Matplotlib & Pandas** – Libraries used to analyze the collected data and generate visualizations such as bar charts, helping users interpret their digital stress results.
4. **Heroku** – Cloud platform used for project deployment, providing users access to the application in a live terminal environment.

<!--
1. HTML - Used to build the basic structure of the website.
2. CSS - Styles the front-end to create a visually appealing design and enhance user experience.
3. Balsamiq - Used to design wireframes and plan the layout of the site before development.
4. JS -  Adds interactivity to the website, making the experience more dynamic and engaging for users.

*Webaim
[Tested contrast](https://webaim.org/resources/contrastchecker/)
*Coolors
[Tested color](https://coolors.co/contrast-checker/33008a-f8f8ff)

_Main color palette_
![Main color Palette](assets/images/readme/PalletColors.png)
-->

---


## ✨ Features

### 🚀 Existing Features

- **Digital Stress Survey**  
  A command-line survey that asks users about screen time, social media use, emotional well-being, and lifestyle habits to evaluate digital stress levels.

- **Personalized Feedback**  
  Based on user answers, the program generates tailored insights and practical recommendations to help reduce digital fatigue and improve wellness.

- **Visual Charts**  
  Using Matplotlib, the app generates bar charts that help users understand their digital behavior and stress impact in a visual, easy-to-read format.

- **Data Logging via Google Sheets**  
  Every survey submission is stored securely in a connected Google Sheet using the `gspread` library, allowing for long-term tracking and analysis.

- **Automatic Score Calculation**  
  The app calculates a digital stress score using weighted inputs across several areas, offering objective, data-driven feedback.

- **Deployed on Heroku**  
  The application is hosted online using Heroku, making it accessible from any device with internet access and a terminal interface.

- **Clear User Prompts**  
  Friendly, easy-to-follow instructions guide users through the survey, even if they are not tech-savvy.

- **Repeatable Use**  
  Users can retake the survey multiple times, and new results will be stored alongside previous entries for ongoing self-assessment.

---


<!--
### HTML Files
  ### 1. Home Page: index.html

  Headline Prompt:

  - HOME: "Needs Bookkeeping?" – A clear, central question targeting the user’s intent.

  - Background Image: A professional, finance-related image (charts and a hand with a pen) that supports the bookkeeping theme.

  - Call-to-Action (CTA) Buttons:

    - Quick Quiz – Likely leads to an interactive assessment to evaluate bookkeeping needs.

    - Check This! – Possibly redirects to a page with useful bookkeeping facts or tips.

    - Play & Save! – An engaging gamified option to win discounts or special offers.

  - Visual Styling: High contrast between button text (white) and button background (dark purple).

  - Very dark green header text helps capture attention.

  - Central alignment of all content for focus and simplicity.

  - Transparent background or slight blur behind text for better readability on the image.
    
  ![quickQuiz_page](assets/images/readme/Webpgs/home.png)
-->

---

<!--
### CCS Files
Currently, all styles are consolidated in a single CSS file (quiz.css) for simplicity.
1. quiz.css – Contains all custom styling for the website, including layout, typography, color schemes, button designs, responsive behavior, and section-specific formatting across all pages.

---

### JS Files.
1. index.js – Manages all logic related to the homepage, including navigation and event handling for the three main buttons: Quiz, Check This!, and Play & Save!.

-->
---

### 🔮 Features Left to Implement

1. **PDF Summary Export (Coming Soon)**  
   Users will be able to download a PDF summary of their responses, results, and wellness recommendations for personal tracking or sharing with a health professional.

2. **Historical Trends Dashboard**  
   A feature to visualize stress patterns over time using saved data from multiple entries (e.g., line graphs comparing past scores).

3. **Web App Interface**  
   Expand the current CLI tool into a browser-accessible version with buttons, forms, and interactive charts using Flask or Django.

4. **Email Reports (Optional)**  
   Option to send results and wellness tips to the user’s email after completing the survey.

5. **Smart Tips Based on Age Group**  
   Deliver more personalized feedback and wellness strategies based on the user's age bracket.

6. **External Resource Integration**  
   Include links to guided meditation apps, breathing exercises, or curated articles based on user’s stress level.

7. **Timestamped Submissions (Commig Soon)**  
  Each entry is logged with a date and time, enabling users to compare past and present results to monitor trends and improvement.

<!--
-   Gamified Experience: A fun quiz mode that unlocks new tips based on performance.
-   Progress Badge System: Motivates users to improve and track their digital well-being.
-->



<!--
1. **Performance Optimization**  
   Further streamline scripts and assets to improve load times and Lighthouse scores.

Business structure insights (LLC, S-Corp, Sole Prop, etc.)
The game will deliver practical, easy-to-understand content that helps users make smarter business and tax decisions, all while keeping the learning experience enjoyable.
-->
---

## 🧑‍💻 Languages Used
-   [Python 3](https://www.python.org/doc/) – Main programming language used to build the logic and functionality of the digital stress survey.
-   [Markdown](https://en.wikipedia.org/wiki/Markdown) – Used to create this README file with clear formatting and structure.

<!--
-   [HTML5](https://en.wikipedia.org/wiki/HTML5) Hypertext Markup Language.
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) Cascading Style Sheets.
-   [JS](https://en.wikipedia.org/wiki/JavaScript) JavaScript.
-->

---

## 🧰 Frameworks, Libraries & Programs Used
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
2. [GitHub:](https://github.com/)
3. [Visual Studio Code:](https://code.visualstudio.com/)
    - Visual Studio Code for code editor with AI.
    - GitHub is used to store the projects code after being pushed from Git.
4. [CI Python Linter:](https://pep8ci.herokuapp.com/)
    - Python Validator (pep8ci)
5. [Youtube](https://www.youtube.com/)
    - YouTube
6. [W3 Schools]( https://www.w3schools.com/)
    - W3 Schools


<!--
1. [Bootstrap 5.3.3:](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website. This framework helps designing websites. It includes HTML and CSS based design templates for typography, forms, buttons, tables, navigation, modals, image carousels, etc. It also gives you support for JavaScript plugins. 
2. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
3. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
4. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes. Designers love the use of icons as fonts because of the flexibility of styling available with high-quality iconography on every device.
5. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript. JQuery for DOM manipulation.
6. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
7. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
8. [Visual Studio Code:](https://code.visualstudio.com/)
    - Visual Studio Code for code editor with AI.
9. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
    - Photoshop was used for editing photos for the website.
10. [Squoosh:]( https://squoosh.app/)
    - Sqoosh App to resize or compress image files, and change file extension for the website.
11. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://balsamiq.cloud/s45whoh/p56wz1i/r2278) during the design process.
12. [Responsive Screenshots](https://ui.dev/amiresponsive)
    - To capture responsive screenshots across devices.
13. [Contrast Checker](https://webaim.org/resources/linkcontrastchecker/?fcolor=CDA37C&bcolor=FFFF00)
    - Webaim Contrast Checker.
14. [Coolors](Coolorshttps://coolors.co/)
    - Coolors App is a pallet generator & pallet visualizer.
15. Lighthouse by Google-Inspect
    - Generate a Lighthouse report by Google: Performance, Accesibility, Best Practices, and SEO.
16. [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - W3C Markup Validator
17. [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - W3C CSS Validator
18. [Youtube](https://www.youtube.com/)
    - YouTube
19. [Pexels]( https://www.pexels.com/)
    - Pexels
20. [W3 Schools]( https://www.w3schools.com/)
    - W3 Schools

-->

---

## 🧪 Testing & Validation
### ✅ Browser & Device Testing  
- Web browsers: Chrome, Firefox, Safari, and Microsoft Edge.
-  On mobile devices: iPhone 13 Mini, Pixel 7 Pro.
-  On laptops: MacBook Pro 14”, MacBook Pro 16”.
<!--
- DevTools used for responsive checks 
-  The navigation, pages, and content sections are clear, readable, and easy to navigate.
- The form validation works correctly: required fields enforce input, email fields only accept valid formats, and the submit buttons function as expected.
-->

---

### ✅ Validator Testing
<!--
- HTML: W3C Markup Validator  
- CSS: W3C CSS Validator  
- JavaScript: JSHint – no errors 
-->

- Python: CI Python Linter [https://pep8ci.herokuapp.com/]

These tools ensured that all pages were free of syntax errors and followed best coding practices.

---
<!--
## HTML
  All pages have passed the official W3C Markup Validator with no errors.

### Home Page

  #### Home Page: [`index.html`](index.html)
  This is the landing page titled **"Needs Bookkeeping?"** where users begin their experience.
  ![Home Page](assets/images/readme/W3C-Markup/W3C-index.html%20(quickquiz).png)

---

## CSS
All pages have passed the official W3C CSS Validator with no errors.

  #### Quiz
  #### Informational Page: [`quiz.css`](quiz.css)
  ![quiz CSS](assets/images/readme/W3-CSS/W3C-quiz.css.png)

---

## JS
All pages have passed the official JSHint with no errors.

  #### Index
  #### Informational Page: [`index.js `](index.js)
  ![Index JS](assets/images/readme/JSHint/JSH-index.js.png)

---

### ✅ Accessibility Testing
- Lighthouse DevTools by Google
### Home Page and Quiz Flow
  #### Home Page: [`index.html`](index.html)
  ![Lighthouse DevTools Home](assets/images/readme/Lighthouse/LH-index.html.png)

  ---

### ✅ Console in Google Chrome DevTools-"Inspect" Testing
- Console Error Testing using Google Chrome DevTools

  Each page was tested via the Console tab in Chrome's Developer Tools to detect and resolve any JavaScript or resource-related issues. All known 404, syntax, or runtime errors were addressed, ensuring a clean console output across the site.

-->

### 🧑‍💻 Testing User Stories – User Experience (UX) Evaluation

#### First-Time Visitor Goals

🔰 First-Time Visitor Goals
1. **Understand the Survey’s Purpose Quickly**
    - Upon arrival, users are welcomed with a clear introduction to the survey’s goals: understanding the connection between digital habits and stress.
    - A brief overview explains how the app works, why it's beneficial, and how the results can support digital well-being.

2. **Complete the Survey in Under 5–10 Minutes**
    - The survey is intentionally designed to be short and focused, taking no longer than 5–10 minutes to complete.

    - Questions use plain, user-friendly language with simple input formats (e.g., numbers, yes/no, checkboxes) to minimize time and confusion.

3. **Receive Personalized Feedback Based on Answers**
    - After submission, users receive immediate, meaningful feedback through data visualizations and tailored recommendations.

    - Compare user responses to group averages, and tips are dynamically generated to support improved digital wellness.

4. **Feel Confident That Data is Handled Respectfully and Securely**
    - Users are assured that their responses are anonymous, not shared with third parties, and stored securely.

    - A short message before the survey reinforces the privacy policy and encourages honest participation without fear of judgment.

<!--
1. **Understand the Site's Purpose and Offerings Quickly**
   - Upon arrival, users are greeted with a clean layout featuring clearly labeled buttons and intuitive navigation.
   - The site uses visually appealing background images, a vibrant color palette, and strong contrast for optimal readability.
   - Calls-to-action (CTAs) are prominently placed, encouraging users to begin exploring key services or features.

2. **Navigate Effortlessly and Discover Relevant Content**
   - The site structure is fluid and user-friendly, allowing seamless transitions between pages.
   - Each section is purpose-driven, with dynamic content that aligns with the user's needs or interests.

3. **Feel Visually Engaged and Motivated to Explore**
   - First-time users encounter a visually compelling design that captures attention and invites exploration.
   - Interactive elements and engaging content foster curiosity and encourage deeper engagement with the site.

4. **Easily Find Contact Information and Trust Signals**
   - Contact options are clearly presented and accessible across all pages.
   - Customer testimonials or reviews are integrated to build credibility and foster trust with new visitors.
-->

#### Returning Visitor Goals

As a Returning Visitor, I want to:

1. **Take the Survey Again and Compare Results Over Time**  
   - Returning users can easily access the survey to reflect on their digital stress habits periodically.  
   - While full history tracking may be a future enhancement, users are encouraged to retake the survey and note changes manually for now.

2. **See Insights Based on Group Averages**  
   - Results include comparisons between the user’s data and aggregated averages from all previous submissions.  
   - This helps users understand how their digital habits align with broader trends and whether they fall within healthy ranges.

3. **Receive a Summary of Responses and Tips**  
   - Users have the option to review a summary of their answers directly on-screen.  
   - *(Optional future feature)* Exportable or email-ready summaries may be included to help users track personal progress and apply wellness tips more effectively.

---

#### Frequent User Goals

As a Frequent User, I want to:
1. **Track Digital Stress Patterns and Improvements**  
   - Frequent users can regularly complete the survey to reflect on progress and changes in their digital stress habits.  
   - This encourages awareness and motivates ongoing self-improvement over time.

2. **View Visual Summaries of Key Metrics**  
   - The app provides information to compare screen time, app usage (e.g., social media, games), and stress levels.  
   - These visuals help users understand their digital behavior trends in a clear and engaging way.

3. **Explore Wellness Tips and Mindfulness Support**  
   - Users are presented with actionable wellness tips based on their results.  
   - *(Optional future enhancement)* Integration with external resources such as mindfulness apps, breathing exercises, or digital detox guides may be included for deeper support.

<!--
1. **Easily Access and Submit IRS Form 1040**
   - Fill out and submit the IRS Form 1040 through a simple and secure on-site form.

2. **View Helpful Financial Comparisons for Smarter Decisions**
   - Quickly review side-by-side comparisons such as **LLC vs. S-Corp** structures with graphics.
   - Use this information to make informed decisions about taxes, bookkeeping needs, or business structure changes.
-->

#### Further Testing
- The Python-based survey was rigorously tested in **multiple terminal environments** (macOS Terminal, Windows Command Prompt, VS Code terminal) to confirm compatibility and proper console rendering.
- Cross-platform testing was carried out on **Windows, macOS, and Linux**, ensuring consistent functionality regardless of the user’s operating system.
- The survey was also tested on **Heroku’s cloud-based interface**, verifying that **Google Sheets integration**, **data storage**, and **graph generation (via Matplotlib)** worked seamlessly in the deployed environment.
- Functionality tests confirmed that:
  - All **survey input prompts** accepted expected responses and handled invalid inputs gracefully.
  - **Graphs and visual feedback** were generated correctly based on user data.
  - **Google Sheets updates** occurred in real-time with appropriate data validation.
- **UX testing** was conducted with a small group of users (ages 18–55) who provided feedback on the **clarity of questions**, **usefulness of recommendations**, and **overall flow** of the survey.
- Suggestions from testers led to improvements in:
  - Labeling and feedback for input errors  
  - Layout and clarity of the survey output  
  - Enhanced tips based on stress levels and screen time results

<!-->
- The website was thoroughly tested across major web browsers, including **Google Chrome**, **Safari**, **Microsoft Edge**, and even **Internet Explorer** to ensure cross-browser compatibility.
- Device testing was conducted on a range of platforms, including **desktop and laptop computers**, as well as mobile devices such as **iPhone 7, iPhone 8, and iPhone X**.
- Comprehensive internal testing was performed to confirm that **all internal and external links functioned correctly**, and that navigation between pages was smooth and intuitive.
- Usability testing involved feedback from **friends and family members**, who were invited to explore the site and identify any bugs, broken functionality, or areas of improvement from a user experience (UX) perspective.
-->
---

### 🐞 Bugs
### Solved Bugs
- Fixed a bug where invalid user inputs (e.g., text instead of numbers) caused the program to crash — added input validation with user-friendly error messages.
- Resolved an issue where survey results were not being saved correctly to **Google Sheets** due to incorrect column indexing.
- Corrected logic in stress-level feedback: users with minimal screen time were previously receiving incorrect high-stress recommendations.
- Removed redundant variables and cleaned up unused imports to improve code readability and efficiency.
- Verified that no exceptions appear in the terminal or on Heroku deployment logs after full survey completion.
- Improved wording and grammar in survey prompts and feedback messages for better UX clarity and professionalism.

<!--
- Significant bugs were identified and resolved across all major development areas, including **HTML5**, **CSS3**, and **JavaScript**.
- Several spelling and grammar issues were corrected throughout the project to improve clarity and professionalism.
- Improved navigation by adding functional Back/Home buttons to return to the main page.
- Resolved JavaScript syntax errors to ensure cleaner and more maintainable code.
- Verified in Google Chrome Developer Tools that the console is free of errors after inspection for each page.
-->
---
### Unsolved Bugs / Areas for Improvement
- **Survey restart flow**: Currently, users must manually restart the script to retake the survey. A built-in "Retake Survey" option would improve usability.
- **Data overwrite risk**: There's a minor risk of overwriting rows in Google Sheets if manual edits are made directly in the sheet without preserving structure.
- **Graph display on some environments**: On rare occasions, the Matplotlib graph window fails to open in certain headless or minimal-terminal environments (e.g., some Linux setups or cloud-based IDEs).
- **No authentication for repeated entries**: Users can take the survey multiple times without any session tracking. Future improvements could include a timestamp or user ID column to track submissions.
- **Limited mobile support**: Since this is a terminal-based app, mobile users may not be able to interact without a physical keyboard or SSH terminal app.
- **UI limitations**: Although the console interface works well, a future web-based version with buttons, sliders, and real-time feedback would improve accessibility and visual appeal.
<!--
- **CSS cleanup**: Some unused or redundant CSS rules should be removed to reduce file size and improve maintainability.
- **Code optimization**: Grouping and organizing code by section or page can make it easier to deploy, reduce the likelihood of bugs, and improve performance.
- **Lighthouse Performance**: The site's performance metrics (as measured by Google's Lighthouse tool) can be improved by further optimizing code, assets, and loading behavior.
-->
---


## 📥 Deployment

### 🌐 GitHub Pages Deployment (For Frontend Projects)

The project was successfully deployed to **GitHub Pages** using the steps below:

1. Log in to GitHub and open your project’s [repository](https://github.com/).
2. At the top of the repository (below the repo name, not the site header), click on the **"Settings"** tab.
   - Alternatively, view a GIF tutorial by clicking [Link to GitHub Docs](https://raw.githubusercontent.com/).
3. In the left-hand sidebar under **"Code and Automation"**, click on **"Pages"**.
4. On the GitHub Pages screen, scroll down to the **"Source"** section.
5. Click the dropdown that says **"None"** and select **"Master Branch"** (or **"main"**, if that's your default).
6. The page will refresh automatically and display the deployment status.
7. Scroll down again to find the live URL of your published site under the **"GitHub Pages"** section.
   - Example: [https://your-username.github.io/your-repo-name](https://github.com)

You can now access your project live on the web using the provided GitHub Pages URL.

### 🍴 Forking the GitHub Repository

  Forking a GitHub repository allows you to create a personal copy of the original project in your own GitHub account. This enables you to freely explore, modify, or contribute without affecting the original codebase. Follow these steps:

  1. Log in to GitHub and open the target [GitHub Repository](https://github.com/).
  2. At the top-right corner of the repository page (just above the "Settings" tab), click the **"Fork"** button.
  3. GitHub will create a copy of the repository under your own account.
  4. You can now freely edit, update, and experiment within your forked version without impacting the original repository.

### 📂 Making a Local Clone

  Follow these steps to create a local copy of the repository on your machine:
   
  1. Log in to GitHub and navigate to the target [GitHub Repository](https://github.com/).
  2. Below the repository name, click the **"Code"** button (formerly "Clone or download").
  3. Under **"Clone with HTTPS"**, copy the provided URL.
  4. Open **Git Bash** (or your terminal of choice).
  5. Change the current working directory to the location where you want the cloned project to reside.
  6. Type the following command and paste the URL you copied in Step 3:
  
    git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

  7. Press Enter. Git will create a full local clone of the repository:

    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY


  Cloning into 'project-folder'or `CI-Clone`...
  remote: Counting objects: 10, done.
  remote: Compressing objects: 100% (8/8), done.
  remote: Total 10 (delta 1), reused 10 (delta 1)
  Unpacking objects: 100% (10/10), done.
  

📎 For additional guidance and visual steps, visit GitHub’s official help guide:
Cloning a repository – GitHub Docs

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

### Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

### 🚀 Heroku Deployment (For Python Backend Project)

The Python-based Digital Stress Survey was deployed to **Heroku** using the following steps:

1. Ensure your project includes the following essential files:
   - `requirements.txt` — listing all dependencies (e.g., `gspread`, `matplotlib`, `pandas`, etc.)
   - `Procfile` — containing the command to run your app (e.g., `python app.py`)
   - `runtime.txt` — specifying the Python version (e.g., `python-3.11.4`)
   - `creds.json` — your Google Sheets API credentials (added securely via Heroku config vars, **not committed** to GitHub)

2. Push your final project to GitHub.

3. Log in to your [Heroku dashboard](https://dashboard.heroku.com/) and follow these steps:
   - Click **“New” → “Create new app”**.
   - Choose a unique app name and select your region.
   - Click **Create app**.
      - #### Creating the Heroku app

        When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

        1. `heroku/python`
        2. `heroku/nodejs`

        You must then create a _Config Var_ called `PORT`. Set this to `8000`

        If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

4. Under **"Deploy"**, choose **GitHub** as the deployment method.
   - Connect your GitHub account if prompted.
   - Search for and connect your repository.
   - #### Constraints
      The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

5. Scroll down to **Manual Deploy** and click **Deploy Branch**.
   - Once complete, click **View App** to launch your live Python survey.

6. (Optional but recommended) Go to **Settings → Config Vars** and:
   - Add your Google Sheets API credentials (`CREDS`) as a JSON string.
   - Add any environment variables needed securely here.

> Your app is now live on Heroku and ready to collect survey data and display insights!

---

## 🙏 Credits & Acknowledgements
* Code Institute

### Code, Resources & References

<!--
- [Stack Overflow](https://stackoverflow.com)  
  Used for troubleshooting and researching common development issues during the project.
- [Bootstrap 5.3.3 Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)  
  Bootstrap library was used throughout the project to create a responsive layout using the Bootstrap Grid System.
  -->

- [Google](https://www.google.com)  
  Utilized for general development research, code examples, and technical clarification.


### 📚 Content

- The **survey structure**, question flow, and recommendations were designed and written by the developer based on personal research and user testing.

- I used the Code Institute’s projects as inspiration for flow and formatting:
  - [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode
Public)
  - [Love Sandwiches](https://github.com/cynthiapinedoh79/love_sandwiches)

- Survey questions were influenced by research into **digital wellness**, **screen fatigue**, and **behavioral psychology**.

- 🧠 **Educational & Research Sources** that inspired the stress evaluation and feedback logic:
  1. [Verywell Mind – Digital Stress and Mental Health](https://www.verywellmind.com/)
  2. [American Psychological Association – Stress in America Report](https://www.apa.org/news/press/releases/stress)
  3. [Harvard Health – Technology and Mental Health](https://www.health.harvard.edu/)
  4. [World Health Organization – Digital Health and Wellbeing](https://www.who.int/health-topics/digital-health)
  5. [Psychology Today – Screen Time Effects](https://www.psychologytoday.com/us/topics/screen-time)


<!--
* I used as example from the Code Institute's [Fun Coding Facts]
* I used as example from the Code Institute's [Love Maths]( https://github.com/cynthiapinedoh79/Love-Maths) project.

-   Content was written by developer.

- 💡 **Color Psychology Resources** (used for chart color choices and feedback aesthetics):
  1. [Color Psychology](https://www.colorpsychology.org/)
  2. [Canva – Color Meanings](https://www.canva.com/colors/color-meanings/)
  3. [Color Matters](https://www.colormatters.com/)
  4. [Academia.edu – Psychological Properties of Colour (Angela Wright)](https://www.academia.edu/)
  5. [Verywell Mind – Color Psychology](https://www.verywellmind.com/color-psychology-2795824)

> These sources helped ensure that the content was both insightful and rooted in well-being principles.
-->

### Media

<!--
- [freestocks](https://freestocks.org/)
- [pixabay](https://pixabay.com/)
- [unsplash](https://unsplash.com/)
- [pexels](https://pexels.com/)
-->

### 🙏 Acknowledgements

- I would like to express my sincere gratitude to the **Code Institute support team** (mentor, tutor and Student Care) for their unwavering guidance and encouragement throughout the development of this project.
- A special thanks to my mentor, Medale Oluwafemi, whose insightful advice, constructive feedback, and continuous support were instrumental to my progress.
- Appreciation to the Code Institute Slack community for their valuable assistance and shared insights during moments of challenge.
- My heartfelt thanks go to **Code Institute** for offering an exceptional course that laid the foundation for this project and significantly advanced my learning journey.
- Finally, I was inspired by the diverse and creative example projects showcased by **Code Institute**, which helped shape and refine the vision for my own work.

---

