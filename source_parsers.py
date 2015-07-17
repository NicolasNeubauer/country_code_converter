from HTMLParser import HTMLParser

class CarParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.start = False
        self.table = []
        self.start = False
        self.currentRow = []
        self.currentCol = 0

        
    def handle_starttag(self, tag, attrs):
        if tag=='tbody':
            self.start = True
            return

        if not self.start:
            return

        if tag=='tr':
            self.currentRow = []
            self.table.append(self.currentRow)
            self.currentCol=0


    def handle_data(self, data):
        if not self.start:
            return
        if data == "\n":
            return
        if self.currentCol > 2:
            return
        
        self.currentRow.append(data)
        self.currentCol += 1

class CCParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.start = False
        self.table = []
        self.start = False
        self.currentRow = []
        self.currentCol = 0
        self.ignoreNext = False

        
    def handle_starttag(self, tag, attrs):
        if tag=='tbody':
            self.start = True
            return

        if not self.start:
            return

        if tag=='tr':
            self.currentRow = []
            self.table.append(self.currentRow)
            self.currentCol=0

        if tag=='span':
            if attrs:
                for name, value in attrs:
                    if name=='style' and value == 'display:none;':
                        self.ignoreNext = True
                        break
        

    def handle_data(self, data):
        if not self.start:
            return
        if data == "\n":
            return
        if self.currentCol > 3:
            return
        if self.ignoreNext:
            self.ignoreNext = False
            return
        
        self.currentRow.append(data)
        self.currentCol += 1
        
