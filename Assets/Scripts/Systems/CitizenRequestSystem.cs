using System;
using System.Collections.Generic;
using UnityEngine;

[Serializable]
public class CitizenRequest
{
    public int id; public string category; public string title; public string district; public string status; public int reward; public int cost;
}

public class CitizenRequestSystem : MonoBehaviour
{
    public static CitizenRequestSystem Instance { get; private set; }
    public List<CitizenRequest> requests = new();
    int nextId = 101;
    readonly string[] categories = {"Road Repair","Streetlight","Water Shortage","Garbage Collection","Traffic Problem","Park Maintenance"};
    readonly string[] districts = {"Central","Riverside","Northgate","East Tech","Old Town","Green Park"};
    void Awake(){ Instance=this; }
    public void TryGenerateRequest(CityState s)
    {
        if (requests.Count >= 8 || UnityEngine.Random.value > .18f) return;
        string c=categories[UnityEngine.Random.Range(0,categories.Length)];
        requests.Add(new CitizenRequest{id=nextId++,category=c,title=c+" request",district=districts[UnityEngine.Random.Range(0,districts.Length)],status="Pending",cost=UnityEngine.Random.Range(1200,6500),reward=UnityEngine.Random.Range(1,4)});
        CityManager.Instance?.Raise("New citizen request: "+c, CityManager.AlertLevel.Info);
    }
    public void Resolve(CitizenRequest r)
    {
        if(r==null||r.status=="Resolved") return;
        if(CityManager.Instance.Spend(r.cost, r.category)) { r.status="Resolved"; CityManager.Instance.State.happiness=Mathf.Clamp(CityManager.Instance.State.happiness+r.reward,0,100); CityManager.Instance.Raise("Citizen request resolved: "+r.category,CityManager.AlertLevel.Success); }
    }
    public void Reject(CitizenRequest r){ if(r!=null&&r.status=="Pending") { r.status="Rejected"; CityManager.Instance.State.happiness=Mathf.Clamp(CityManager.Instance.State.happiness-1.5f,0,100); CityManager.Instance.Notify(); } }
}
