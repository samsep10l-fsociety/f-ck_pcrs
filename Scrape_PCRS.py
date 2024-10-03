# Designed and Engineered by samsep10l --fsociety

from bs4 import BeautifulSoup
import re


def get_formatted_questions():

    html_content = "[Body of PCRS HTML Goes here...]"

    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract multiple-choice questions
    mc_questions = extract_multiple_choice_questions(soup)

    # Extract coding questions
    coding_questions = extract_coding_questions(soup)

    # Combine both lists
    QUESTIONS = mc_questions + coding_questions

    # Initialize the list to hold formatted question tuples
    formatted_questions = []

    # Process the QUESTIONS list and format each question into a single string
    for question in QUESTIONS:
        for title, content in question.items():
            question_str = f"Question Title: {title}\n"
            if isinstance(content, dict):  # Multiple-choice question
                question_str += f"Question:\n{content['question']}\n"
                question_str += f"Number of Options: {content['options_count']}\n"
                question_str += "Options:\n"
                for idx, option in enumerate(content['options'], 1):
                    question_str += f"{idx}. {option}\n"
                question_str += "Which one of these options is correct!"
            elif isinstance(content, list):  # Coding question
                question_str += f"Question:\n{content[0]}\n"
                question_str += "Code Provided:\n"
                question_str += f"{content[1]}\n"
                question_str += "Complete the code asked."
            # Add the formatted question string to the list along with the title
            formatted_questions.append((title, question_str))

    return formatted_questions





def extract_multiple_choice_questions(soup):
    QUESTIONS = []
    questions_divs = soup.find_all('div', id=re.compile('multiple_choice-'))
    for div in questions_divs:
        # Extract the question title
        question_title_tag = div.find('p', class_='widget_title')
        if question_title_tag:
            question_title = question_title_tag.get_text(strip=True)
        else:
            continue  # Skip if no title

        # Extract the question text
        question_header = div.find('h5', class_='problem-description')
        if question_header:
            question_text = question_header.get_text(separator=' ', strip=True)
        else:
            continue  # Skip if no question text

        # Extract the options
        options = []
        form = div.find('form')
        if form:
            labels = form.find_all('label', class_='checkbox')
            for label in labels:
                code_tag = label.find('code')
                if code_tag:
                    option_text = code_tag.get_text(strip=True)
                    options.append(option_text)
                else:
                    option_text = label.get_text(separator=' ', strip=True)
                    options.append(option_text)
            options_count = len(options)
            if options_count == 0:
                continue  # Skip if no options
        else:
            continue  # Skip if no form

        # Create the question dictionary
        question_dict = {
            question_title: {
                'question': question_text,
                'options_count': options_count,
                'options': options
            }
        }
        # Append to QUESTIONS list
        QUESTIONS.append(question_dict)
    return QUESTIONS

def extract_coding_questions(soup):
    QUESTIONS = []
    code_divs = soup.find_all('div', id=re.compile('python-'))
    for div in code_divs:
        # Extract the question title
        question_title_tag = div.find('p', class_='widget_title')
        if question_title_tag:
            question_title = question_title_tag.get_text(strip=True)
        else:
            continue  # Skip if no title

        # Extract the question text
        question_header = div.find('h5', class_='problem-description')
        if question_header:
            question_text = question_header.get_text(separator=' ', strip=True)
        else:
            continue  # Skip if no question text

        # Extract the code
        code_div = div.find('div', class_='CodeMirror-code')
        if code_div:
            code_lines = code_div.find_all('pre')
            code = '\n'.join([pre.get_text() for pre in code_lines])
        else:
            continue  # Skip if no code provided

        # Create the question dictionary
        question_dict = {
            question_title: [question_text, code]
        }
        # Append to QUESTIONS list
        QUESTIONS.append(question_dict)
    return QUESTIONS
