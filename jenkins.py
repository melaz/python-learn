__author__ = 'Dmitry'
import jenkins
j = jenkins.Jenkins('http://tdw-deploy-tool.dbdc.luxoft.com:8080/jenkins/')
j.get_jobs()
j.create_job('empty', jenkins.EMPTY_CONFIG_XML)



from autojenkins import Jenkins
j = Jenkins('http://tdw-deploy-tool.dbdc.luxoft.com:8080/jenkins/')
j.get_config_xml('Test-run')

j = Jenkins('http://jenkins.pe.local')