# pig-latin-translator

# notes for future improvements
- could possibly make code cleaner by using:
	-   .capitalize instead of .lower/.upper
	-   using false to mark when there's no capitalization
	-   try/except blocks for errors instead of using for loops

- need to try to break program with
	-   double punctuation
	-   multiple spaces
	-   line breaks

- still need to figure out
	-   how to handle quotation marks at the beginning of words
	-   name with 1 letter plus an apostrophe looks weird after translation, need to move apostrophe with letter
	-   contractions with I also need remedied
	-   if last word in phrase, don´t add space
	-   abbreviations with titles ex. dr. mr. mrs. etc
	-   other punctuation symbols
		- 	dash, hyphen, slash, etc

- think i´ve got figured out
	-   making sure all input characters are valid
	-   ending punctuation
	-   beginning capitalization (middle and ending capitalization is fine to leave as is)
	-   bug when words have only one letter
