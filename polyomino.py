# coding=utf-8
r"""
Polyomino classes

AUTHORS:

- Alexandre Blondin Massé
- Simon Désaulniers
- Sébastien Labbé
- Franco Saliola
- Jérôme Tremblay

"""
#************************************************************************************
#  Copyright (C) 2013 Alexandre Blondin Massé <alexandre.blondin.masse@gmail.com    *
#                     Simon Désaulniers <rostydela@gmail.com>                       *
#                     Sébastien Labbé <slabqc@gmail.com>,                           *
#                     Franco Saliola <saliola@gmail.com>                            *
#                     Jérôme Tremblay <jerome.tremblay@gmail.com>                   *
#                                                                                   *
#  Distributed under the terms of the GNU General Public License version 2 (GPLv2)  *
#                                                                                   *
#  The full text of the GPLv2 is available at:                                      *
#                                                                                   *
#                  http://www.gnu.org/licenses/                                     *
#************************************************************************************

#######################################################################
#                                                                     #
#                    Abstract polyomino class                         #
#                                                                     #
#######################################################################

class Polyomino_class:
    pass

#######################################################################
#                                                                     #
#                    Basic data type classes                          #
#                                                                     #
#######################################################################

class PolyominoDatatype_matrix:

    def __init__(self, matrix):
        self._matrix = matrix

    def __repr__(self):
        return 'Polyomino of %s cells' % self.area()

    def area(self):
        return sum(row.count(1) for row in self._matrix)

class PolyominoDatatype_boundary:

    def __init__(self, boundary):
        self._boundary = boundary

    def __len__(self):
        return len(self._boundary)

    def __repr__(self):
        return 'Polyomino of perimeter %s' % len(self)

#######################################################################
#                                                                     #
#                    Concrete polyomino classes                       #
#                                                                     #
#######################################################################

class Polyomino_matrix(PolyominoDatatype_matrix, Polyomino_class):
    pass

class Polyomino_boundary(PolyominoDatatype_boundary, Polyomino_class):
    pass

