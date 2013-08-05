import sublime, sublime_plugin


# From http://www.sublimetext.com/forum/viewtopic.php?f=5&t=5513
class Move_caret_forwardCommand(sublime_plugin.TextCommand):
    def run(self, edit, nlines):

        (row, col) = self.view.rowcol(self.view.sel()[0].begin())
        target = self.view.text_point(row + nlines, col)

        self.view.sel().clear()
        self.view.sel().add(sublime.Region(target))
        self.view.show(target)


class Move_caret_backCommand(sublime_plugin.TextCommand):
    def run(self, edit, nlines):
        screenful = self.view.visible_region()

        (row,col) = self.view.rowcol(self.view.sel()[0].begin())
        target = self.view.text_point(row-nlines, col)

        self.view.sel().clear()
        self.view.sel().add(sublime.Region(target))
        self.view.show(target)