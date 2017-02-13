# wlbl

This is still a work in progress and shouldn't be used by anyone

##The Idea

IP whitelists for your stuff.
The dream:
- Users and groups with acls and hierarchies
- IP lists and groups with ports
- Distributed update method (decentralized possibly using select clients as secondary servers in the event primary is down)
- Blacklist hooks and whatnot (Think fail2ban with a posthook)
- Multiple update methods (pubkey primary goal atm)


##What Works

Nothing yet.

##What Doesn't

Auth

##Milestones

Milestone 1:
- Working Connexion API (barebones)
- basic iptables rule generation for v4 (No ports, groups, etc)

##Notes

RFCs for allowed ip ranges in the config (private, reserved, etc) can be found [on the ipaddress module doc page](https://docs.python.org/3/library/ipaddress.html)
