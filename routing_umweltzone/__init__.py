# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RoutingUmweltzone
                                 A QGIS plugin
 Routing außerhalb von Umweltzonen
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-12-02
        copyright            : (C) 2022 by Ludovic Tane
        email                : ludovic.tane@stud.hs-bochum.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
 
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load RoutingUmweltzone class from file RoutingUmweltzone.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .routing_umweltzone import RoutingUmweltzone
    return RoutingUmweltzone(iface)
