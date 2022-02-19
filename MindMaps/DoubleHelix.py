import requests
import json
import time

# -------------------------
# Jinja2
# -------------------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))

# -------------------------
# Headers
# -------------------------
auth_headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

dnac = "https://sandboxdnac.cisco.com"

# -------------------------
# Get OAuth Token
# -------------------------

oAuthTokenRAW = requests.request("POST", f"{ dnac }/dna/system/api/v1/auth/token", headers=auth_headers)
oAuthTokenJSON = oAuthTokenRAW.json()
token = oAuthTokenJSON['Token']

print(token)

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-Auth-Token': token,
}


# -------------------------
# Sites
# -------------------------

sites_template = env.get_template('site.j2')
sitesRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/site/", headers=headers)
sitesJSON = sitesRAW.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = sites_template.render(sites = sitesJSON['response'])

# -------------------------
# Save the markdown file
# -------------------------

with open("DNAC/Sites/Sites.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Site Health
# -------------------------

sitesHealth_template = env.get_template('siteHealth.j2')
sitesHealthRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/site-health/", headers=headers)
sitesHealthJSON = sitesHealthRAW.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = sitesHealth_template.render(siteHealth = sitesHealthJSON['response'])

# -------------------------
# Save the markdown file
# -------------------------

with open("DNAC/Sites/Site Health.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Site Memebership (to get at devices)
# -------------------------

sitesMembers_template = env.get_template('siteMembers.j2')
for site in sitesJSON['response']:
        sitesMembersRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/membership/{ site['id'] }", headers=headers)
        sitesMembersJSON = sitesMembersRAW.json()
        if site['name'] == "Global":
                globalSiteID = site['id']
# -------------------------
# Pass to Jinja2 Template 
# -------------------------

        parsed_output = sitesMembers_template.render(
                site = site['name'],
                siteMembers = sitesMembersJSON['device']
                )

# -------------------------
# Save the markdown file
# -------------------------

        with open(f"DNAC/Sites/{ site['name'] } Members.md", "w") as fh:
                fh.write(parsed_output)               
                fh.close()

# -------------------------
# VLANs
# -------------------------

vlans_template = env.get_template('vlans.j2')
vlansRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/topology/vlan/vlan-names", headers=headers)
vlansJSON = vlansRAW.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = vlans_template.render(vlans = vlansJSON['response'])

# -------------------------
# Save the markdown file
# -------------------------

with open(f"DNAC/Topology/VLANs.md", "w") as fh:
        fh.write(parsed_output)               
        fh.close()

# -------------------------
# VLAN Topologies
# -------------------------

for vlan in vlansJSON['response']:
        vlanToplogy_template = env.get_template('l2_topology.j2')
        vlanTopologyRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/topology/l2/{ vlan }", headers=headers)
        vlanTopologyJSON = vlanTopologyRAW.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

        parsed_output = vlanToplogy_template.render(
                vlan = vlan,
                vlanTopology = vlanTopologyJSON['response']
                )

# -------------------------
# Save the markdown file
# -------------------------

        with open(f"DNAC/Topology/VLANs/{ vlan } Topology.md", "w") as fh:
                fh.write(parsed_output)               
                fh.close()

# -------------------------
# Physical Topology
# -------------------------

physical_template = env.get_template('physical_topology.j2')
physicalRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/topology/physical-topology", headers=headers)
physicalJSON = physicalRAW.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = physical_template.render(vlanTopology = vlanTopologyJSON['response'])

# -------------------------
# Save the markdown file
# -------------------------

with open(f"DNAC/Topology/Physical Topology.md", "w") as fh:
        fh.write(parsed_output)               
        fh.close()

# -------------------------
# L3 Topologies
# -------------------------

protocols = ['ospf','eigrp','isis','static']
for protocol in protocols:
        l3Toplogy_template = env.get_template('l3_topology.j2')
        l3TopologyRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/topology/l2/{ protocol }", headers=headers)
        l3TopologyJSON = l3TopologyRAW.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

        parsed_output = l3Toplogy_template.render(
                protocol = protocol,
                l3Topology = l3TopologyJSON['response'])

# -------------------------
# Save the markdown file
# -------------------------

        with open(f"DNAC/Topology/RoutingProtocols/{ protocol } Topology.md", "w") as fh:
                fh.write(parsed_output)               
                fh.close()

# -------------------------
# Topology Health
# -------------------------

networkHealth_template = env.get_template('network_health.j2')
networkHealthRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-health", headers=headers)
networkHealthJSON = networkHealthRAW.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = networkHealth_template.render(
        DNAC = dnac,
        health = networkHealthJSON,
        )

# -------------------------
# Save the markdown file
# -------------------------

with open(f"DNAC/Network Health.md", "w") as fh:
        fh.write(parsed_output)               
        fh.close()

# -------------------------
# Get All Devices
# -------------------------

devicesRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-device/", headers=headers)
devicesJSON = devicesRAW.json()

# -------------------------
# Link Mismatch - VLAN
# -------------------------

insightVlanRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-device/insight/{ globalSiteID }/device-link?category=vlan", headers=headers)
insightVlanJSON = insightVlanRAW.json()

# -------------------------
# Link Mismatch - Speed Duplex
# -------------------------

insightSpeedDuplexRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-device/insight/{ globalSiteID }/device-link?category=speed-duplex", headers=headers)
insightSpeedDuplexJSON = insightSpeedDuplexRAW.json()

# -------------------------
# Device Health
# -------------------------

healthRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/device-health/", headers=headers)
healthJSON = healthRAW.json()

for device in devicesJSON['response']:

# -------------------------
# Base Details per Device
# -------------------------

        device_template = env.get_template('device.j2')
        deviceRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-device/{ device['id'] }", headers=headers)
        deviceJSON = deviceRAW.json()

# -------------------------
# Chassis per Device
# -------------------------

        deviceChassisRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-device/{ device['id'] }/chassis", headers=headers)
        deviceChassisJSON = deviceChassisRAW.json()

# -------------------------
# PowerSupply
# -------------------------

        powerSupplyRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-device/{ device['id'] }/equipment?type=PowerSupply", headers=headers)
        powerSupplyJSON = powerSupplyRAW.json()


# -------------------------
# Fan
# -------------------------

        fanRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-device/{ device['id'] }/equipment?type=Fan", headers=headers)
        fanJSON = fanRAW.json()

# -------------------------
# Backplane
# -------------------------

        backplaneRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-device/{ device['id'] }/equipment?type=Backplane", headers=headers)
        backplaneJSON = backplaneRAW.json()

# -------------------------
# Module
# -------------------------

        moduleRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-device/{ device['id'] }/equipment?type=Module", headers=headers)
        moduleSON = moduleRAW.json()

# -------------------------
# PROCESSOR
# -------------------------

        processorRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-device/{ device['id'] }/equipment?type=PROCESSOR", headers=headers)
        processorJSON = processorRAW.json()

# -------------------------
# Other
# -------------------------

        otherRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-device/{ device['id'] }/equipment?type=Other", headers=headers)
        otherJSON = otherRAW.json()

# -------------------------
# PoE
# -------------------------

        poeRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-device/{ device['id'] }/interface/poe-detail", headers=headers)
        poeJSON = poeRAW.json()

# -------------------------
# VLANs
# -------------------------

        deviceVlanRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-device/{ device['id'] }/vlan", headers=headers)
        deviceVlanJSON = deviceVlanRAW.json()

# -------------------------
# Interfaces
# -------------------------

        interfacesRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/interface/network-device/{ device['id'] }", headers=headers)
        interfacesJSON = interfacesRAW.json()

# -------------------------
# Stack
# -------------------------

        stackRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/network-device/{ device['id'] }/stack", headers=headers)
        stackJSON = stackRAW.json()

# -------------------------
# Compliance
# -------------------------

        complianceRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/compliance/{ device['id'] }/detail", headers=headers)
        complianceJSON = complianceRAW.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

        parsed_output = device_template.render(
                device = deviceJSON['response'],
                chassis = deviceChassisJSON['response'],
                powersupply = powerSupplyJSON['response'],
                fan = fanJSON['response'],
                backplane = backplaneJSON['response'],
                module = moduleSON['response'],
                processor = processorJSON['response'],
                other = otherJSON['response'],
                poe = poeJSON['response'],
                vlan = deviceVlanJSON['response'],
                insightVLAN = insightVlanJSON['response'],
                insightSpeedDuplex = insightSpeedDuplexJSON['response'],
                interfaces = interfacesJSON['response'],
                stack = stackJSON['response'],
                health = healthJSON['response'],
                compliance = complianceJSON['response']
                )

# -------------------------
# Save the markdown file
# -------------------------

        with open(f"DNAC/Devices/{ device['hostname'] }.md", "w") as fh:
                fh.write(parsed_output)               
                fh.close()

# -------------------------
# SWIM
# -------------------------

swim_template = env.get_template('swim.j2')
swimRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/image/importation", headers=headers)
swimJSON = swimRAW.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = swim_template.render(
        DNAC = dnac,
        swim = swimJSON['response'],
        )

# -------------------------
# Save the markdown file
# -------------------------

with open(f"DNAC/SWIM/SWIM.md", "w") as fh:
        fh.write(parsed_output)               
        fh.close()

# -------------------------
# Projects
# -------------------------

projects_template = env.get_template('projects.j2')
projectsRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/template-programmer/project", headers=headers)
projectsJSON = projectsRAW.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = projects_template.render(
        DNAC = dnac,
        projects = projectsJSON,
        )

# -------------------------
# Save the markdown file
# -------------------------

with open(f"DNAC/Projects/Projects.md", "w") as fh:
        fh.write(parsed_output)               
        fh.close()

# -------------------------
# Templates
# -------------------------

templates_template = env.get_template('templates.j2')
for item in projectsJSON:
        for template in item['templates']:
                templatesRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/template-programmer/template/{ template['id'] }", headers=headers)
                templatesJSON = templatesRAW.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

                parsed_output = templates_template.render(
                        project = item['name'],
                        template = templatesJSON,
                        )

# -------------------------
# Save the markdown file
# -------------------------

                with open(f"DNAC/Templates/{ template['name'] } Template.md", "w") as fh:
                        fh.write(parsed_output)               
                        fh.close()

# -------------------------
# RF Profiles
# -------------------------

rfProfile_template = env.get_template('rf_profiles.j2')
rfProfileRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/wireless/rf-profile", headers=headers)
rfProfileJSON = rfProfileRAW.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = rfProfile_template.render(
        DNAC = dnac,
        rfProfiles = rfProfileJSON['response'],
        )

# -------------------------
# Save the markdown file
# -------------------------

with open(f"DNAC/Wireless/RF Profiles.md", "w") as fh:
        fh.write(parsed_output)               
        fh.close()

# -------------------------
# Assurance Test Results
# -------------------------

assuranceTest_template = env.get_template('assurance_tests.j2')
assuranceTestsRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/AssuranceGetSensorTestResults", headers=headers)
assuranceTestsJSON = assuranceTestsRAW.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = assuranceTest_template.render(
        DNAC = dnac,
        assurance_tests = assuranceTestsJSON['response']['summary'],
        )

# -------------------------
# Save the markdown file
# -------------------------

with open(f"DNAC/Assurance/Assurance Sensor Test Results.md", "w") as fh:
        fh.write(parsed_output)               
        fh.close()

# -------------------------
# Flow Analysis
# -------------------------

flowAnalysis_template = env.get_template('flow_analysis.j2')
flowAnalysisRAW = requests.request("GET", f"{ dnac }/dna/intent/api/v1/flow-analysis", headers=headers)
flowAnalysisJSON = flowAnalysisRAW.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = flowAnalysis_template.render(
        DNAC = dnac,
        flow_analysis = flowAnalysisJSON['response'],
        )

# -------------------------
# Save the markdown file
# -------------------------

with open(f"DNAC/Flow Analysis/Flow Analysis.md", "w") as fh:
        fh.write(parsed_output)               
        fh.close()  