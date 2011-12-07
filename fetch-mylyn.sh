#!/bin/sh

rm -fr org.eclipse.mylyn

for f in \
org.eclipse.mylyn \
org.eclipse.mylyn.bugzilla.core \
org.eclipse.mylyn.bugzilla-feature \
org.eclipse.mylyn.bugzilla.ide \
org.eclipse.mylyn.bugzilla.tests \
org.eclipse.mylyn.bugzilla.ui \
org.eclipse.mylyn.commons.core \
org.eclipse.mylyn.commons.net \
org.eclipse.mylyn.commons.ui \
org.eclipse.mylyn.compatibility \
org.eclipse.mylyn.context.core \
org.eclipse.mylyn.context-feature \
org.eclipse.mylyn.context.tests \
org.eclipse.mylyn.context.ui \
org.eclipse.mylyn.discovery.core \
org.eclipse.mylyn.discovery.ui \
org.eclipse.mylyn-feature \
org.eclipse.mylyn.help.ui \
org.eclipse.mylyn.ide.ant \
org.eclipse.mylyn.ide.dev \
org.eclipse.mylyn.ide-feature \
org.eclipse.mylyn.ide.tests \
org.eclipse.mylyn.ide.ui \
org.eclipse.mylyn.java-feature \
org.eclipse.mylyn.java.tasks \
org.eclipse.mylyn.java.tests \
org.eclipse.mylyn.java.ui \
org.eclipse.mylyn.monitor.core \
org.eclipse.mylyn.monitor-feature \
org.eclipse.mylyn.monitor.tests \
org.eclipse.mylyn.monitor.ui \
org.eclipse.mylyn.monitor.usage \
org.eclipse.mylyn.pde-feature \
org.eclipse.mylyn.pde.ui \
org.eclipse.mylyn.resources.tests \
org.eclipse.mylyn.resources.ui \
org.eclipse.mylyn.tasks.bugs \
org.eclipse.mylyn.tasks.core \
org.eclipse.mylyn.tasks.tests \
org.eclipse.mylyn.tasks.ui \
org.eclipse.mylyn.team.cvs \
org.eclipse.mylyn.team-feature \
org.eclipse.mylyn.team.tests \
org.eclipse.mylyn.team.ui \
org.eclipse.mylyn.tests \
org.eclipse.mylyn.trac.core \
org.eclipse.mylyn.trac-feature \
org.eclipse.mylyn.trac.tests \
org.eclipse.mylyn.trac.ui \
org.eclipse.mylyn.web.tasks-feature \
org.eclipse.mylyn.web.tasks \
org.eclipse.mylyn.wikitext-feature \
org.eclipse.mylyn.wikitext.confluence.core \
org.eclipse.mylyn.wikitext.confluence.ui \
org.eclipse.mylyn.wikitext.core \
org.eclipse.mylyn.wikitext.help.ui \
org.eclipse.mylyn.wikitext.mediawiki.core \
org.eclipse.mylyn.wikitext.mediawiki.ui \
org.eclipse.mylyn.wikitext.tasks.ui \
org.eclipse.mylyn.wikitext.tests \
org.eclipse.mylyn.wikitext.textile.core \
org.eclipse.mylyn.wikitext.textile.ui \
org.eclipse.mylyn.wikitext.tracwiki.core \
org.eclipse.mylyn.wikitext.tracwiki.ui \
org.eclipse.mylyn.wikitext.twiki.core \
org.eclipse.mylyn.wikitext.twiki.ui \
org.eclipse.mylyn.wikitext.ui \
org.eclipse.mylyn.cdt-feature \
org.eclipse.mylyn.cdt.ui \
; do
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/tools \
export -r R_3_3_1_e_3_5 org.eclipse.mylyn/$f;
done

tar cjf org.eclipse.mylyn-R_3_3_1-fetched-src.tar.bz2 org.eclipse.mylyn
