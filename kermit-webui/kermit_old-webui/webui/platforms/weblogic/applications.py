'''
Created on Oct 25, 2011

@author: mmornati
'''
import logging
from webui.platforms.weblogic.utils import extract_appli_info, check_contains,\
    extract_appli_details
from webui.platforms.abstracts import Application
from webui.platforms.platforms import platforms
from webui.platforms.weblogic import settings
from webui.serverdetails import utils


logger = logging.getLogger(__name__)

class WebLogicApplication(Application):
    
    def getApplications(self, user):
        servers = utils.extract_user_servers(user)
        #Retrieving applilist for any server controlled by kermit
        applications = []
        for server in servers:
            environment = self.extract_environment_level(server)           
            appli = extract_appli_info(server.hostname, environment)
            if appli:
                for app in appli:
                    extracted = check_contains(applications, app)
                    if extracted:
                        extracted["deploy"] = extracted["deploy"] + 1
                        extracted["servers"].append(app["servers"])
                    else:
                        applications.append(app)
    
        return applications
    
    def getApplicationsPath(self, user, server_path):
        servers = utils.extract_user_servers_in_path(user, server_path)
        #Retrieving applilist for any server controlled by kermit
        applications = []
        for server in servers:
            environment = self.extract_environment_level(server)           
            appli = extract_appli_info(server.hostname, environment)
            if appli:
                for app in appli:
                    extracted = check_contains(applications, app)
                    if extracted:
                        extracted["deploy"] = extracted["deploy"] + 1
                        extracted["servers"].append(app["servers"])
                    else:
                        applications.append(app)
    
        return applications
    
    def getAppliInfo(self, user, appname):
        servers = utils.extract_user_servers(user)
        #Retrieving applilist for any server controlled by kermit
        applications = []
        for server in servers:
            environment = self.extract_environment_level(server)
            appli = extract_appli_details(server.hostname, environment, appname)
            if appli:
                applications.extend(appli)
        return applications
    
platforms.register(WebLogicApplication, settings.PLATFORM_NAME)