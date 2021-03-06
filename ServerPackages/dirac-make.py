#!/usr/bin/env python

import imp, os, sys, platform, shutil

here = os.path.dirname( os.path.abspath( __file__ ) )
chFilePath = os.path.join( os.path.dirname( here ) , "common", "CompileHelper.py" )
try:
  fd = open( chFilePath )
except Exception, e:
  print "Cannot open %s: %s" % ( chFilePath, e )
  sys.exit( 1 )

chModule = imp.load_module( "CompileHelper", fd, chFilePath, ( ".py", "r", imp.PY_SOURCE ) )
fd.close()
chClass = getattr( chModule, "CompileHelper" )

ch = chClass( here )

versions = { 'mock' : "0.7.1",
             'Sphinx' : '1.0.7',
             'rst2pdf' : '0.16',
             'nose' : '1.0',
             'pylint' : '0.23.0',
             'coverage' : '3.4',
             'pexpect' : '3.3' }

ch.setPackageVersions( versions )

for package in versions:
  packageToInstall = "%s>=%s" % ( package, versions[ package ] )
  if not ch.easyInstall( packageToInstall ):
    ch.ERROR( "Could not deploy %s with easy_install" % package )
    if not ch.pip( packageToInstall ):
      ch.ERROR( "Could not deploy %s with pip" % package )
      sys.exit( 1 )
