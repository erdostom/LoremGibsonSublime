import sublime
import sublime_plugin
import re
import random
import urllib


class LoremgibsonCommand(sublime_plugin.TextCommand):
    @classmethod
    def scrapesite(self):
        myText = []
        raw = urllib.request.urlopen("http://loremgibson.com").read().decode("utf-8")
        regex1 = re.compile("myText\[\d+\].*;")
        var_lines = regex1.findall(raw)
        regex2 = re.compile("myText\[\d+?\] = \"([a-zA-Z- ]+)\";")
        for line in var_lines:
            r = regex2.search(line.strip('\n'))
            if r:
                item = r.groups()[0]
                myText.append(item)
        random.shuffle(myText)
        out = " ".join(myText[0:72])
        return out

    def run(self, edit):
        out = LoremgibsonCommand.scrapesite()
        self.view.insert(edit, self.view.sel()[0].begin(), out)
