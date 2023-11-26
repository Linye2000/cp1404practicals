import wikipedia

def main():
    """Main function to interactively search Wikipedia pages."""
    while True:
        # Prompt the user for a page title or search phrase
        title = input("Enter a page title or search phrase: ")

        # Exit the loop if the input is empty
        if not title:
            break

        try:
            # Get the Wikipedia page without automatic redirection
            page = wikipedia.page(title, auto_suggest=False)

            # Display the page title, summary, and URL
            print("Title:", page.title)
            print("Summary:", wikipedia.summary(title))
            print("URL:", page.url)

        except wikipedia.DisambiguationError as e:
            # Handle disambiguation errors
            print("Disambiguation error. Please be more specific. Options include:", e.options)

        except wikipedia.PageError:
            # Handle page not found errors
            print("Page not found. Please try a different title.")

        except Exception as e:
            # Handle any other exceptions
            print("An error occurred:", e)


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()