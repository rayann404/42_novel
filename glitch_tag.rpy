init python:
    class GlitchText(renpy.Displayable):
        def __init__(self, child, amount, **kwargs):
            super(GlitchText, self).__init__(**kwargs)
            if isinstance(child, (str, unicode)):
                self.child = Text(child)
            else:
                self.child = child
            self.amount = amount

        def render(self, width, height, st, at):
            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            y = 0
            while y < self.height:
                glitch_occurs = renpy.random.random() * 100 < self.amount
                if glitch_occurs:
                    curr_height = renpy.random.randint(-10,10)
                else:
                    curr_height = renpy.random.randint(0,10)
                curr_offset = renpy.random.randint(-10,10)
                curr_surface = child_render.subsurface((0,y,self.width,curr_height))
                if glitch_occurs:
                    render.subpixel_blit(curr_surface, (curr_offset, y))
                else:
                    render.subpixel_blit(curr_surface, (0, y))
                if curr_height > 0:
                    y += curr_height
                else:
                    y -= curr_height
            renpy.redraw(self,0)
            return render

    # Argument is the percertage of the time it'll apply a random offset to a randomly sized slice.
    # offset_percent: (Float between 0.0-100.0) Percentage chance a random block of the render will be offset.
    # 0 will cause it to never occur. 100 will cause an offset on every line.
    # Example: {glitch=59.94}Text{/glitch}
    def glitch_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            argument = 10.0
        else:
            argument = float(argument)
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                char_disp = GlitchText(my_style.apply_style(text), argument)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = GlitchText(my_img, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    config.custom_text_tags["glitch"] = glitch_tag
