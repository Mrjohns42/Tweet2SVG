#! /usr/bin/env python

import os
from textwrap import wrap

DEFAULT_WIDTH = 3207
DEFAULT_HEIGHT = 791
DEFAULT_FONT_SIZE = 150

class SVGMaker():	
	
	def __init__(self,batch_start=0):
		self.batch=batch_start
		self.imagepath = "images/batch%d"
		self.svg_header = """<?xml version="1.0"?> \n""" \
						+ """<svg width="%d" height="%d" xmlns="http://www.w3.org/2000/svg"> \n""" \
						+ """<g> \n""" 
		
		self.svg_text = """<text x="%d" y="%d" font-size="%d" font-family="%s" stroke="%s" fill="%s">%s</text> \n"""
		
		self.svg_footer = """</g> \n""" \
				 		+ """</svg>"""
		self.newCanvas()

	
	def newCanvas(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, font_size=DEFAULT_FONT_SIZE):
		self.WIDTH = width
		self.HEIGHT = height
		self.FONT_SIZE = font_size

		self.FONT_FAMILY = "monospace"

		self.FONT_WIDTH = 0.6 * self.FONT_SIZE
		self.FONT_HEIGHT = self.FONT_SIZE
		
		self.X_POS = 10
		self.Y_POS = self.FONT_SIZE

		self.CHAR_LIMIT =  int( (self.WIDTH  - self.X_POS)            / self.FONT_WIDTH  )
		self.TWEET_LIMIT = int( (self.HEIGHT - 0.25*self.FONT_HEIGHT) / self.FONT_HEIGHT )
		
		# self.batchpath = self.imagepath%self.batch
		# if not os.path.exists(self.batchpath):
		# 	os.makedirs(self.batchpath)
			
		self.batch += 1	
		self.tweet_count = 0
		

	def code_svg(self, text, x, y, stroke_color="#000000", fill_color="#000000"):
		code = unicode(self.svg_header) % (self.WIDTH, self.HEIGHT)
		for n,line in enumerate(wrap(text, self.CHAR_LIMIT)):
			code += unicode(self.svg_text) % (x, y + (self.FONT_HEIGHT * n), self.FONT_SIZE, self.FONT_FAMILY, stroke_color, fill_color, line)
		code += unicode(self.svg_footer)

		return code

	def create_svg(self, text):
		#create new canvas if necessary
		# if self.tweet_count >= self.TWEET_LIMIT:
		# 	self.newCanvas()

		#apply character limit
		# text = text[:self.CHAR_LIMIT]

		#fill parameters into svg code
		svg_code = self.code_svg(text, self.X_POS, self.Y_POS)
		#svg_code = removeNonAscii(svg_code)

		#write svg to file
		imagefile = "images/tweet%d.svg" % self.tweet_count	
		with open(imagefile, 'w') as f:
			f.write(svg_code.encode("UTF-8"))

		#update counter
		self.tweet_count += 1

			
		
def main():
	svg=SVGMaker()
	for i in range(100):
		svg.create_svg("The quick brown fox jumped over the lazy dogs %d"%i)


if __name__ == '__main__':
	main()
