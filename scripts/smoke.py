from pathlib import Path
import json,re,subprocess,time
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as contract_actions

R=Path(__file__).parents[1];ROOT=R.parents[3]
def env(name):
 text=(ROOT/'accounts.env').read_text();m=re.search(r'^'+re.escape(name)+r'\s*=\s*"?([^"\r\n]+)',text,re.M);return m.group(1).strip()
def calldata(method=None,args=None,kwargs=None):
 out={}
 if method is not None:out['method']=method
 if args:out['args']=args
 if kwargs:out['kwargs']=kwargs
 return out
contract_actions.make_calldata_object=calldata
accounts=[create_account(account_private_key=env('ACCOUNT_'+str(i)+'_GENLAYER_PRIVATE_KEY')) for i in (1,2,3)];clients=[create_client(chain=studionet,account=a) for a in accounts];address=json.loads((R/'deployment.json').read_text())['contractAddress'];sha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();stamp=str(int(time.time()));case='CHARTER-'+stamp
raw='https://raw.githubusercontent.com/warnedwarn/parallel-statute/'+sha+'/evidence/';cdn='https://cdn.jsdelivr.net/gh/warnedwarn/parallel-statute@'+sha+'/evidence/'
def send(client,method,args):
 tx=client.write_contract(address=address,function_name=method,args=args);client.wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000);full=client.get_transaction(transaction_hash=tx);leader=(full.get('consensus_data',{}).get('leader_receipt')or[{}])[0];assert full.get('result_name')=='MAJORITY_AGREE' and leader.get('execution_result')=='SUCCESS',full;return str(tx)
txs={};txs['register']=send(clients[1],'register_instrument',[case,accounts[2].address,'Harbor Access Charter','English','Tamazight',['Article 1 access','Article 2 appeal deadline','Article 3 language assistance'],raw+'left-text.md',cdn+'right-text.md',900]);txs['audit']=send(clients[2],'audit_parity',[case]);mid=clients[1].read_contract(address=address,function_name='get_instrument',args=[case]);assert mid['state']=='DRIFT',mid;txs['repair']=send(clients[1],'repair_text',[case,'RIGHT',cdn+'right-text-corrected.md']);state=clients[1].read_contract(address=address,function_name='get_instrument',args=[case]);assert state['state']=='RESTORED',state;out={'instrumentId':case,'transactions':txs,'state':state,'walletDisclosure':'All demo wallets and bilingual excerpts are operator-controlled fixtures.'};(R/'network-run.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
