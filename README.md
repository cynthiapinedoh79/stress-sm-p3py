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
1. Professionals & remote workers – people experiencing screen fatigue or tech overload.
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
      3. I may want to download or receive a summary of my responses and tips.

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
  User-Centered Flow:
  The questions follow a logical and empathetic order — starting with basic habits and gently leading into emotional well-being — ensuring users never feel overwhelmed or judged.

  Clarity & Simplicity:
  Instructions and questions are short, jargon-free, and formatted with consistent spacing for readability in the terminal.

  Immediate Feedback:
  Upon completion, users receive personalized summaries, visual graphs (via Matplotlib), and practical recommendations based on their responses.

  Purposeful Interactivity:
  Users engage in a step-by-step format that feels natural and smooth, including options to skip non-relevant sections and retry invalid inputs without frustration.

  Visual & Analytical Layer:
  While text-based in interaction, the app enhances insights with bar graphs that compare the user’s habits to average data from others — making results feel more relevant and motivating.

  Trust & Privacy Focus:
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
Our objective is to create a website that is both professional and functional. Our focus is on design that is both intuitive and creative.

![Strategy](assets/images/readme/fivePlanes/strategy.png)

### 📐 Scope
The site is designed for two main user groups:
1.	Visitors, who can enjoy interactive games, helpful tips, new information, and practical advice.
2.	Potential new customers, who can explore special offers like a bookkeeping bonus award, contact us easily, or quickly access the Form 1040 submission link.

![Scope pg1](assets/images/readme/fivePlanes/scope1.png)

![Scope pg2](assets/images/readme/fivePlanes/scope2.png)

### 🏗️ Structure
The website is designed with HTML5, CSS3 and JS.

**Website Pages:**
1. **_Needs Bookkepping?:_** Main page with three buttons (Quiz, Check This! and Play & Save!)
2. **_Quiz:_** A brief quiz with a few questions that are scored to assess user needs.
3. **_Feedback:_** A feedback message is shown if your answers indicate that you may need our help or services. It includes a link to fill out Form 1040 and a direct link to contact us through our website.
4. **_CheckThis:_** Displays Bookkeeping Fact Cards with useful information.
6. **_Prize:_** Try Your Luck! Win a special prize or bookkeeping bonus—just reach out to claim your reward!

![Structure](assets/images/readme/fivePlanes/structure.png)

### 🦴 Skeleton
The website is designed to be clear and simple. And the site has a simple tree structure with hierarchical flows from top to bottom.

<!--
**Wireframe**
The wireframe is designed using Balsamiq software 
[Balsamic](https://balsamiq.cloud/ss26tqg/p4441iq/rD01A)

#### Home
![Home](assets/images/readme/Bals/Bals-Home.png)
-->

### 🎨 Surface
To create a pleasing and understandable view, I opt for natural colors such as earth, green, and a range of tones that complement and contrast each other.

---

## 🛠️ Technologies & Design Choices
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

---

## ✨ Features

### 🚀 Existing Features

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

1. **Performance Optimization**  
   Further streamline scripts and assets to improve load times and Lighthouse scores.

Business structure insights (LLC, S-Corp, Sole Prop, etc.)
The game will deliver practical, easy-to-understand content that helps users make smarter business and tax decisions, all while keeping the learning experience enjoyable.

---

## 🧑‍💻 Languages Used

<!--
-   [HTML5](https://en.wikipedia.org/wiki/HTML5) Hypertext Markup Language.
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) Cascading Style Sheets.
-   [JS](https://en.wikipedia.org/wiki/JavaScript) JavaScript.
-->

---

## 🧰 Frameworks, Libraries & Programs Used

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


#### Returning Visitor Goals

As a Returning Visitor, I want to:

1. **Access More Detailed Information About Services**
   - Gain deeper insights into the services offered, including descriptions, pricing, and available packages.
   - View updated details such as business hours, availability, and seasonal offerings.

2. **Quickly Find the Best Way to Get in Touch**
   - Locate contact methods without effort, whether it's through a dedicated contact page, live chat, or email.
   - Know who to reach out to for specific inquiries or support needs.

3. **Understand Available Communication Options**
   - Clearly see if meetings or consultations are offered via Zoom, Skype, phone calls, or in-person appointments.
   - Choose the most convenient method for follow-ups or service discussions.

---

#### Frequent User Goals

As a Frequent User, I want to:

1. **Easily Access and Submit IRS Form 1040**
   - Fill out and submit the IRS Form 1040 through a simple and secure on-site form.

2. **View Helpful Financial Comparisons for Smarter Decisions**
   - Quickly review side-by-side comparisons such as **LLC vs. S-Corp** structures with graphics.
   - Use this information to make informed decisions about taxes, bookkeeping needs, or business structure changes.


#### Further Testing

- The website was thoroughly tested across major web browsers, including **Google Chrome**, **Safari**, **Microsoft Edge**, and even **Internet Explorer** to ensure cross-browser compatibility.
- Device testing was conducted on a range of platforms, including **desktop and laptop computers**, as well as mobile devices such as **iPhone 7, iPhone 8, and iPhone X**.
- Comprehensive internal testing was performed to confirm that **all internal and external links functioned correctly**, and that navigation between pages was smooth and intuitive.
- Usability testing involved feedback from **friends and family members**, who were invited to explore the site and identify any bugs, broken functionality, or areas of improvement from a user experience (UX) perspective.

---

### 🐞 Bugs
### Solved Bugs

- Significant bugs were identified and resolved across all major development areas, including **HTML5**, **CSS3**, and **JavaScript**.
- Several spelling and grammar issues were corrected throughout the project to improve clarity and professionalism.
- Improved navigation by adding functional Back/Home buttons to return to the main page.
- Resolved JavaScript syntax errors to ensure cleaner and more maintainable code.
- Verified in Google Chrome Developer Tools that the console is free of errors after inspection for each page.

---
### Unsolved Bugs / Areas for Improvement

- **CSS cleanup**: Some unused or redundant CSS rules should be removed to reduce file size and improve maintainability.
- **Code optimization**: Grouping and organizing code by section or page can make it easier to deploy, reduce the likelihood of bugs, and improve performance.
- **Lighthouse Performance**: The site's performance metrics (as measured by Google's Lighthouse tool) can be improved by further optimizing code, assets, and loading behavior.

---


## 📥 Deployment
### 🌐 GitHub Pages Deployment

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

---

## 🙏 Credits & Acknowledgements
* Code Institute
* Dette Bookkeeping: Website [Dette Bookkeeping & More, LLC]( https://dette-bookkeeping.com/)

### Code, Resources & References

- [Stack Overflow](https://stackoverflow.com)  
  Used for troubleshooting and researching common development issues during the project.
- [Bootstrap 5.3.3 Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)  
  Bootstrap library was used throughout the project to create a responsive layout using the Bootstrap Grid System.
- [Google](https://www.google.com)  
  Utilized for general development research, code examples, and technical clarification.

### Content
* I used as example from the Code Institute's [Fun Coding Facts]
* I used as example from the Code Institute's [Love Maths]( https://github.com/cynthiapinedoh79/Love-Maths) project.

-   Content was written by developer.

-   Free Color Psychology Resources
1.	Color Psychology
→ In-depth guide on how colors affect behavior, mood, and decision-making.
2.	Canva – Color Meanings
→ Visual and practical breakdown of color symbolism in design and branding.
3.	Color Matters
→ Educational resource on color symbolism, theory, and real-world impact.
4.	Psychological Properties of Colours – Academia.edu
→ A scholarly article on color psychology by Angela Wright.
5.	Verywell Mind – Color Psychology
→ Psychology-backed overview on how color influences emotions and perception.


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




































This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
