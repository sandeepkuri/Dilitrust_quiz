class Elements(object):

    # Website page links and variables

    # Amazon Page elements and Variables

    AMAZON_HOME = 'https://www.amazon.ca/'
    SAMSUNG_TV = 'Samsung-Ultra-QN49Q60RAFXZC-Canada-Version/dp/B07NC7DTDG/'
    SEARCH_VALUE = 'samsung tv'
    samsung_results = '"samsung tv"'

    amazon_element = {
        "search_imput": "//input[@id='twotabsearchtextbox']",
        "search_button": "//div[@class='nav-search-submit nav-sprite']//input[@class='nav-input']",
        "search_results": "//span[@class='a-color-state a-text-bold'][text()='"+samsung_results+"']",
        "zero_item": "//span[@id='nav-cart-count'][text()='0']",
        "add_tv": "//input[@id='add-to-cart-button']",
        "verify_item": "//h1[@class='a-size-medium a-text-bold'][contains(text(),'Added to Cart')]"
    }

    # Google Page elements and Variables

    GOOGLE_DRIVE_PAGE = 'https://drive.google.com/drive/folders/12StEdmmTe_xkulh-diGMrk2yenRMplsq'

    google_elements = {
        "log_in": "//a[contains(text(), 'Sign in')]",
        "email_address": "//input[@id='identifierId']",
        "b_next": "//span[contains(text(), 'Next')]",
        "password": "//input[@name='password']",
        "login_verify": "(//div[contains(text(), 'Untitled folder')])[1]",
        "b_new": "//button[@guidedhelpid= 'new_menu_button']",
        "file_upload": "//*[contains(text(),'File upload')]"

    }

    # Aircanada Page elements and Variables

    AIRCANADA_PAGE = "https://www.aircanada.com/"
    FROM = 'Montreal'
    TO = 'Paris'
    timeout = 20
    F_NAME = 'Sandeep'
    L_NAME = "Kuri"
    P_NUMBER = '9999999999'
    EMAIL_ADDRESS = 'sandeepkuri001@gmail.com'

    aircanda_elements = {
        "select_english": "//button[@id='enCAEdition']",
        "from_": "//input[@id='origin_R_0']",
        "from_montreal": "//div[contains(text(),'YUL')]",
        "to_": "//input[@id='destination_R_0']",
        "to_paris": "//div[contains(text(),'CDG')]",
        "select_date": "//span[@class='flight-calendar-label default']",
        "select_02": "//div[@data-monthyear='2020-02']//table[1]//tbody[1]//tr//td[@data-date='02']",
        "select_20": "//div[@data-monthyear='2020-02']//table[1]//tbody[1]//tr//td[@data-date='20']",
        "select_button": "//button[contains(text(),'Select')]",
        "no_flexible": "//span[contains(text(),'My dates are flexible')]",
        "find_button": "//input[@value='	Find']",
        "Select_D_flight": "//li[1]//flight-row[1]//div[1]//div[1]//div[1]//bound-cabin[3]",
        "Select_cl_V": "//div[contains(text(),'Flexible')]/following::button[1]",
        "Select_R_flight": "//li[1]//flight-row[1]//div[1]//div[1]//div[1]//bound-cabin[3]",
        "Select_al_V": "//div[contains(text(),'Flexible')]/following::button[1]",
        "return_flight_page_V": "//span[contains(text(),'Thu - Feb 20')]",

        "continue_after_selection": "//button[@id='submitAvailabilityButton']",
        "book_as_guest": "//button[contains(text(),'Continue as a guest')]",

        "first_name": "//input[@placeholder='FIRST NAME']",
        "last_name": "//input[@placeholder='LAST NAME']",
        "DOB": "//select[@id='DOB_DAY_0']",
        "DOB_02": "//select[@id='DOB_DAY_0']//option[contains(text(),'02')]",
        "MOB": "//select[@id='DOB_MONTH_0']",
        "MOB_FEB": "//select[@id='DOB_MONTH_0']//option[contains(text(),'FEB')]",
        "YOB": "//select[@id='DOB_YEAR_0']",
        "YOB_1997": "//select[@id='DOB_YEAR_0']//option[contains(text(),'1997')]",
        "gender": "//select[@id='GENDER_0']",
        "gender_male": "//select[@id='GENDER_0']//option[contains(text(),'Male')]",
        "C_phone": "//input[@id='COMBINED_PHONE_NO_1_0']",
        "c_email": "//input[@id='CONTACT_EMAIL_1']",
        "Final": "//button[@id='continue']",
    }
