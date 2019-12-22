#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
provider = IBMQ.load_account()


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
provider = IBMQ.load_account()


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
provider = IBMQ.load_account()


# In[1]:


from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister


# In[2]:


q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)


# In[3]:


qc.h(q[0])


# In[4]:


qc.cx(q[0], q[1])


# In[8]:


qc.measure(q, c)


# In[ ]:




