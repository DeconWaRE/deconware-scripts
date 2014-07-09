from com.deconware.algorithms.psf.PsfGenerator import PsfType

class Psf(object):
	def __init__(self, space, emissionWavelength, numericalAperture, lensRefractiveIndex, \
					specimenRefractiveIndex, specimenDepth, homeDirectory="", scopeType=PsfType.WIDEFIELD):
		self.space=space
		self.emissionWavelength=emissionWavelength 
		self.numericalAperture=numericalAperture
		self.lensRefractiveIndex=lensRefractiveIndex 
		self.specimenRefractiveIndex=specimenRefractiveIndex 
		self.specimenDepth=specimenDepth 
		self.homeDirectory=homeDirectory

	def createPsf(self, ops, size):
		return ops.run("psf", size[0], size[2], self.space, self.emissionWavelength, self.numericalAperture, self.lensRefractiveIndex, self.specimenRefractiveIndex, self.specimenDepth)
		
