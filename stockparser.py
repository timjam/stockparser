from HTMLParser import HTMLParser

class stockParser(HTMLParser):
	# Overridable -- handle start tag

    def handle_starttag(self, tag, attrs):

    	pass


    # Overridable -- handle end tag

    def handle_endtag(self, tag):

        pass


    # Overridable -- handle character reference

    def handle_charref(self, name):

        pass


    # Overridable -- handle entity reference

    def handle_entityref(self, name):

        pass


    # Overridable -- handle data

    def handle_data(self, data):

        pass


    # Overridable -- handle comment

    def handle_comment(self, data):

        pass


    # Overridable -- handle declaration

    def handle_decl(self, decl):

        pass


    # Overridable -- handle processing instruction

    def handle_pi(self, data):

        pass


    def unknown_decl(self, data):

        pass