# Emyl's skillets library

<a href="https://www.buymeacoffee.com/emyl79" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## What's a skillet?

Welcome to my skillets collection!

Skillets are snippets of reusable configuration suitable for PAN-OS, the operating system of Palo Alto next-generation firewalls.

For a more detailed introduction, a blog post is coming soon.

## Available collections

There are several types of skillets. At the moment this repository contains only ***panos*** and ***panorama*** skillets, that is small pieces of reusable configuration that can be applied to a firewall or a Panorama instance with a few clicks or commands. More types of skillets will be added shortly.

For each PAN-OS major version (10.1+) a dedicated branch exists. Default branch is currently ***panos_v10.1*** for PAN-OS 10.1.

For each skillet, there's a PAN-OS version and a Panorama version. The latter has the *_panorama* suffix in the skillet name.

Skillets are organized in collections. Below the current list:

### App-ID Collection

* *app_groups*: Common application groups (Active Directory, M365, Sharepoint)

### Content-ID Collection

* *content_id*: IPS profiles with best practice settings and alert settings (anti-virus, anti-spyware, vulnerability protection, Wildfire analysis)
* *url_filtering*: URL Filtering profiles with best practice settings and alert settings

### Network Settings Collection

* *zone_protection*: Zone Protection profiles with best practice settings and customizable flood thresholds

### Reports Collection

* *reports*: Useful reports (currently DNS Security latest threats)

## How to apply skillets

### Panhandler

Install [Panhandler](https://live.paloaltonetworks.com/t5/quickplay-solutions-tools/install-and-get-started-with-panhandler/ta-p/307916), then:

* Login to the web interface (default credentials *paloalto/panhandler*)
* Import this repository
* Run desired skillets from the web interface

### Command line

Install [SLI](https://github.com/PaloAltoNetworks/SLI) with python's *pip* then:
* Clone this repository
* Checkout the desired branch (e.g. *panos_v10_2* for PAN-OS 10.2)
* `cd` to the collection directory
* `sli -n <skillet_name> configure`
* Follow the prompt

## Contributing

Bug reports and contributions using Github issues and pull request are very welcome.

To request a new skillet, please open an issue with the https://github.com/emyl/emyl-skillets-develop/labels/enhancement label so we can discuss.
