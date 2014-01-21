#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:peckj.20140121082121.3904: * @file idiotpie.py
#@@first
#@@language python

#@+<< imports >>
#@+node:peckj.20140121082121.3905: ** << imports >>
#@-<< imports >>
#@+<< declarations >>
#@+node:peckj.20140121082121.3906: ** << declarations >>
#@-<< declarations >>

#@+others
#@+node:peckj.20140121082121.3907: ** class Git
class Git(object):
  #@+others
  #@+node:peckj.20140121082121.3908: *3* __init__
  def __init__(self, name):
    self.name = name
    self.lastCommitId = -1
    master = Branch('master', None)
    self.branches = {}
    self.branches['master'] = master
    self.HEAD = master
  #@+node:peckj.20140121082121.3912: *3* commit
  def commit(self, message):
    self.lastCommitId += 1
    c_id = self.lastCommitId
    commit = Commit(c_id, self.HEAD.commit, message)
    self.HEAD.commit = commit
    return commit
  #@+node:peckj.20140121082121.3913: *3* log
  def log(self):
    commit = self.HEAD.commit
    history = []
    
    while commit is not None:
      history.append(commit)
      commit = commit.parent

    return history
  #@+node:peckj.20140121082121.3916: *3* checkout
  def checkout(self, branchName):
    if branchName in self.branches.keys():
      print 'Switched to existing branch %s' % branchName
      self.HEAD = self.branches[branchName]
    else:
      newBranch = Branch(branchName, self.HEAD.commit)
      self.branches[branchName] = newBranch
      self.HEAD = newBranch
      print 'Switched to new branch %s' % branchName
    return self
  #@-others
#@+node:peckj.20140121082121.3910: ** class Commit
class Commit(object):
  #@+others
  #@+node:peckj.20140121082121.3911: *3* __init__
  def __init__(self, commit_id, parent, message):
    self.commit_id = commit_id
    self.parent = parent
    self.message = message
  #@-others
#@+node:peckj.20140121082121.3914: ** class Branch
class Branch(object):
  #@+others
  #@+node:peckj.20140121082121.3915: *3* __init__
  def __init__(self, name, commit):
    self.name = name
    self.commit = commit
  #@-others
  
#@+node:peckj.20140121082121.3909: ** main
def main():
  print 'branches test'
  repo = Git('test')
  repo.commit('Initial commit')
  repo.commit('Change 1')
  
  def historyToIdMapper(history):
    return "-".join([str(c.commit_id) for c in history])
  
  print 'history (should be 1-0): %s' % historyToIdMapper(repo.log())
  
  repo.checkout('testing')
  repo.commit('Change 2')
  
  print 'history (should be 2-1-0): %s' % historyToIdMapper(repo.log())
  
  repo.checkout('master')
  
  print 'history (should be 1-0): %s' % historyToIdMapper(repo.log())
  
  repo.commit('Change 3')
  print 'history (should be 3-1-0): %s' % historyToIdMapper(repo.log())
#@-others

if __name__=='__main__':
  main()
#@-leo
