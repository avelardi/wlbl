# wlbl

This is still a work in progress and shouldn't be used in production yet.

##The Idea

IP whitelists for your stuff.
The dream:
- Users and groups with acls
- IP lists and groups
- Distributed update method (decentralized possibly using select clients as secondary servers in the event primary is down)
- Blacklist hooks and whatnot (Think fail2ban with a posthook)
- Multiple update methods (pubkey primary goal atm)


##What Works

Nothing yet. 

##What Doesn't

Everything. 

##Milestones

Milestone 1:
- Working Connexion API (barebones)
- basic iptables rule generation for v4 (No ports, groups, etc)
