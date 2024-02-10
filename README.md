# Emyl's skillets library

<a href="https://www.buymeacoffee.com/emyl79" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## What's a skillet?

Welcome to my skillets collection!

Skillets are snippets of reusable configuration suitable for PAN-OS, the operating system of Palo Alto next-generation firewalls.

For a more detailed introduction, you can read [this post on my blog](https://www.buymeacoffee.com/emyl79/the-power-skillets-part-1) dedicated to the argument.

## Available collections

There are several types of skillets available. Description of each type of skillet is out of scope, the best way to start if necessary is [Panhander documentation](https://panhandler.readthedocs.io/en/master/skillets.html).

For each PAN-OS major version (10.1+) a dedicated branch exists. Default branch is currently ***panos_v10.1*** for PAN-OS 10.1.

Each skillet name is prefixed with *emyl_* to avoid possible clash with skillets from other repositories on Panhandler. Moreover, for each configuration skillet, two versions exists: a PAN-OS version and a Panorama version. The latter has the *_panorama* suffix in the skillet name.

Skillets are organized in collections. Below the current list:

### App-ID Collection

* *emyl_app_groups*: Common application groups (Active Directory, M365, Sharepoint)

### Content-ID Collection

* *emyl_content_id*: IPS profiles with best practice settings and alert settings (anti-virus, anti-spyware, vulnerability protection, Wildfire analysis)
* *emyl_panw_edl*: Security policies for blocking traffic to and from Palo Alto predefined IP lists
* *emyl_url_filtering*: URL Filtering profiles with best practice settings and alert settings

### Device Settings Collection

* *emyl_first_setup_workflow*: Workflow for creating ***set*** commands to be applied to the firewall for the very first configuration (e.g. when connected with serial console after first boot)

### Network Settings Collection

* *emyl_zone_protection*: Zone Protection profiles with best practice settings and customizable flood thresholds

### Reports Collection

* *emyl_reports*: Useful reports (currently DNS Security latest threats)

## How to apply skillets

### Panhandler

Install [Panhandler](https://live.paloaltonetworks.com/t5/quickplay-solutions-tools/install-and-get-started-with-panhandler/ta-p/307916), then:

* Login to the web interface (default credentials *paloalto/panhandler*)
* Import this repository
* Run desired skillets from the web interface

### Command line

Install [SLI](https://github.com/PaloAltoNetworks/SLI) with python's *pip* then:
* Clone this repository
* Checkout the desired branch (e.g. *panos_v10.2* for PAN-OS 10.2)
* `cd` to the collection directory
* `sli -n <skillet_name> configure`
* Follow the prompt

## Utilities

Under the **utils** directory there are some useful scripts:

* *sli_add_python_context.py*: a simple Python program that gets standard inputs and populates SLI context, to mimic execution of *python3* skillets.

## Contributing

Bug reports and contributions using Github issues and pull request are very welcome.

To request a new skillet, please open an issue with the https://github.com/emyl/emyl-skillets/labels/enhancement label so we can discuss.
