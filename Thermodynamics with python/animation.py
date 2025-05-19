# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:54:32 2023

@author: HAMID
"""
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

plt.close('all')

class Particle():
    def __init__(self,r=np.zeros(2),v = np.zeros(2),R=1e-2,m=1,color='blue'):
        self.id,self.r,self.v,self.R,self.m,self.color = id,r,v,R,m,color

class Sim():
    X = 10
    Y = 10
    def __init__(self,dt=0.05,Np=20):
        self.dt,self.Np = dt,Np 
        self.particles = [Particle(i) for i in range(self.Np)]
    
    def collision_detection(self):
        ignore_list = []
        for particle1 in self.particles:
            if particle1 in ignore_list:
                continue
            x, y = particle1.r
            if ((x > self.X/2 - particle1.R) or (x < -self.X/2+particle1.R)):
                particle1.v[0] *= -1
            if ((y > self.Y/2 - particle1.R) or (y < -self.Y/2+particle1.R)):
                particle1.v[1] *= -1

            for particle2 in self.particles:
                if id(particle1) == id(particle2):
                    continue
                m1, m2, r1, r2, v1, v2 = particle1.m, particle2.m, particle1.r, particle2.r, particle1.v, particle2.v
                if np.dot(r1-r2, r1-r2) <= (particle1.R + particle2.R)**2:
                    v1_new = v1 - 2*m1 / \
                        (m1+m2) * np.dot(v1-v2, r1-r2) / \
                        np.dot(r1-r2, r1-r2)*(r1-r2)
                    v2_new = v2 - 2*m1 / \
                        (m1+m2) * np.dot(v2-v1, r2-r1) / \
                        np.dot(r2-r1, r2-r1)*(r2-r1)
                    particle1.v = v1_new
                    particle2.v = v2_new
                    ignore_list.append(particle2)
    def increment(self):
        self.collision_detection()
        for particle in self.particles:
            particle.r += self.dt * particle.v
            
    def particle_positions(self):
        return [particle.r for particle in self.particles]
    def particle_colors(self):
        return [particle.color for particle in self.particles]
    def particle_speeds(self):
        return [np.sqrt(np.dot(particle.v,particle.v)) for particle in self.particles]
Np = 200
sim = Sim(Np=Np)

for particle in sim.particles:
    particle.r = np.random.uniform(-sim.X/2,sim.Y/2,size = 2)
    particle.v = 1 + np.array([np.cos(np.pi/4),np.cos(np.pi/4)])
sim.particles[0].color = "red"  

     
fig, (ax,ax2) = plt.subplots(figsize=(5,9),nrows=2)
ax.set_aspect("equal")

vs = np.linspace(0,2,10)

scatter = ax.scatter([],[])
bar = ax2.bar(vs,[0]*len(vs),width=0.9*np.gradient(vs),align='edge',alpha=0.8)


def init():
    ax.set_xlim(-sim.X/2, sim.X/2)
    ax.set_ylim(-sim.Y/2, sim.Y/2)
    ax2.set_xlim(vs[0], vs[-1])
    ax2.set_ylim(0, Np)
    return (scatter,*bar.patches)
def update(frame):
    sim.increment()
    freqs, bins = np.histogram(sim.particle_speeds(),bins=vs)
    for rect,height in zip(bar.patches,freqs):
        rect.set_height(height)
        
    scatter.set_offsets(np.array(sim.particle_positions()))
    scatter.set_color(sim.particle_colors())
    return (scatter,*bar.patches)

ani = FuncAnimation(fig, update, frames=range(2400),init_func = init,blit=True,interval=1/30,repeat=False)






#a = np.array(sim.particle_positions())
#ax.scatter(a[:,0],a[:,1])
#
#sim.increment()
#
#a = np.array(sim.particle_positions())
#ax.scatter(a[:,0],a[:,1])

















