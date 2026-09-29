using System;
using UnityEngine;

public static class CityRandomEventSystem
{
    public static void TryGenerate(CityState s, Action<string, CityManager.AlertLevel> alert)
    {
        // Don't overwrite an existing active decision event
        if (s.currentEvent != null || UnityEngine.Random.value > 0.15f) return;

        int e = UnityEngine.Random.Range(0, 6);
        switch (e)
        {
            case 0:
                s.currentEvent = new DecisionEvent
                {
                    id = "power_failure",
                    title = "⚡ Major Power Failure",
                    description = "Central District has lost main electricity supply due to a transformer blowout. Businesses and hospitals are at risk.",
                    optionA = "Emergency Full Repair (Rs. 15,000)",
                    costA = 15000f,
                    optionB = "Deploy Backup Generators (Rs. 6,000)",
                    costB = 6000f,
                    optionC = "Wait for Normal Crew (Free)",
                    costC = 0f
                };
                alert?.Invoke("CRISIS ALERT: Major Power Failure in Central District!", CityManager.AlertLevel.Critical);
                break;

            case 1:
                s.currentEvent = new DecisionEvent
                {
                    id = "water_pipe_leak",
                    title = "💧 Water Main Break",
                    description = "A primary water pipeline burst near Riverside. Reservoir pressure is dropping rapidly.",
                    optionA = "Replace Main Line (Rs. 12,000)",
                    costA = 12000f,
                    optionB = "Patch & Seal Leak (Rs. 4,500)",
                    costB = 4500f,
                    optionC = "Restrict Water Usage (Free)",
                    costC = 0f
                };
                alert?.Invoke("CRISIS ALERT: Water Main Burst near Riverside!", CityManager.AlertLevel.Warning);
                break;

            case 2:
                s.currentEvent = new DecisionEvent
                {
                    id = "industrial_fire",
                    title = "🔥 Industrial District Fire",
                    description = "A severe fire broke out at a chemical warehouse. Fire units require emergency dispatch funding.",
                    optionA = "Full Emergency Dispatch (Rs. 10,000)",
                    costA = 10000f,
                    optionB = "Standard Fire Response (Rs. 4,000)",
                    costB = 4000f,
                    optionC = "Minimal Containment (Free)",
                    costC = 0f
                };
                alert?.Invoke("CRISIS ALERT: Industrial Fire outbreak reported!", CityManager.AlertLevel.Critical);
                break;

            case 3:
                s.currentEvent = new DecisionEvent
                {
                    id = "pollution_smog",
                    title = "🌫️ Severe Smog & Air Spike",
                    description = "Industrial emissions and heavy traffic created a severe toxic smog cloud over the city.",
                    optionA = "Subsidize Filters & Solar (Rs. 14,000)",
                    costA = 14000f,
                    optionB = "Free Bus Day to cut Traffic (Rs. 5,000)",
                    costB = 5000f,
                    optionC = "Issue Mask Advisory (Free)",
                    costC = 0f
                };
                alert?.Invoke("WARNING: Toxic smog warning issued across districts.", CityManager.AlertLevel.Warning);
                break;

            case 4:
                s.currentEvent = new DecisionEvent
                {
                    id = "tech_boom",
                    title = "🚀 Tech Investment Surge",
                    description = "A major technology enterprise wants to establish a regional innovation hub in your city!",
                    optionA = "Co-Fund Tech Park (Rs. 18,000)",
                    costA = 18000f,
                    optionB = "Grant Tax Relief (Rs. 5,000)",
                    costB = 5000f,
                    optionC = "Standard Approval (Free)",
                    costC = 0f
                };
                alert?.Invoke("OPPORTUNITY: Foreign Tech Enterprise seeking investment approval!", CityManager.AlertLevel.Success);
                break;

            case 5:
                s.trafficEfficiency = Mathf.Clamp(s.trafficEfficiency - 6f, 0, 100);
                s.reservoirLevel = Mathf.Clamp(s.reservoirLevel + 8f, 0, 100);
                alert?.Invoke("WEATHER ALERT: Heavy rainfall is affecting road traffic flow.", CityManager.AlertLevel.Info);
                break;
        }
    }

    public static void ResolveEvent(CityState s, int choice)
    {
        if (s.currentEvent == null) return;
        var ev = s.currentEvent;

        if (ev.id == "power_failure")
        {
            if (choice == 1 && s.budget >= ev.costA)
            {
                s.budget -= ev.costA; s.electricityProduction += 400f; s.happiness += 4f;
                CityManager.Instance?.Raise("Power Failure fully repaired immediately!", CityManager.AlertLevel.Success);
            }
            else if (choice == 2 && s.budget >= ev.costB)
            {
                s.budget -= ev.costB; s.electricityProduction += 150f;
                CityManager.Instance?.Raise("Temporary generators deployed.", CityManager.AlertLevel.Info);
            }
            else
            {
                s.electricityProduction *= 0.88f; s.happiness -= 6f;
                CityManager.Instance?.Raise("Unrepaired power failure caused blackouts & unhappiness.", CityManager.AlertLevel.Critical);
            }
        }
        else if (ev.id == "water_pipe_leak")
        {
            if (choice == 1 && s.budget >= ev.costA)
            {
                s.budget -= ev.costA; s.reservoirLevel += 15f; s.happiness += 3f;
                CityManager.Instance?.Raise("Water Main completely replaced & pressure restored!", CityManager.AlertLevel.Success);
            }
            else if (choice == 2 && s.budget >= ev.costB)
            {
                s.budget -= ev.costB; s.reservoirLevel += 6f;
                CityManager.Instance?.Raise("Water pipe leak patched.", CityManager.AlertLevel.Info);
            }
            else
            {
                s.reservoirLevel -= 12f; s.happiness -= 5f;
                CityManager.Instance?.Raise("Unrepaired leak caused reservoir pressure loss.", CityManager.AlertLevel.Warning);
            }
        }
        else if (ev.id == "industrial_fire")
        {
            if (choice == 1 && s.budget >= ev.costA)
            {
                s.budget -= ev.costA; s.pollution -= 4f; s.happiness += 3f;
                CityManager.Instance?.Raise("Industrial fire extinguished quickly!", CityManager.AlertLevel.Success);
            }
            else if (choice == 2 && s.budget >= ev.costB)
            {
                s.budget -= ev.costB;
                CityManager.Instance?.Raise("Industrial fire contained.", CityManager.AlertLevel.Info);
            }
            else
            {
                s.pollution += 8f; s.happiness -= 7f; s.budget -= 5000f;
                CityManager.Instance?.Raise("Uncontained fire caused heavy structural & environmental damage.", CityManager.AlertLevel.Critical);
            }
        }
        else if (ev.id == "tech_boom")
        {
            if (choice == 1 && s.budget >= ev.costA)
            {
                s.budget -= ev.costA; s.commercialBuildings += 3; s.population += 350; s.happiness += 6f;
                CityManager.Instance?.Raise("Co-funded Tech Park launched! 350 new residents moved in.", CityManager.AlertLevel.Success);
            }
            else if (choice == 2 && s.budget >= ev.costB)
            {
                s.budget -= ev.costB; s.commercialBuildings += 1; s.population += 120;
                CityManager.Instance?.Raise("Tech firm opened regional office.", CityManager.AlertLevel.Success);
            }
            else
            {
                s.population += 40;
                CityManager.Instance?.Raise("Tech firm approved without incentives.", CityManager.AlertLevel.Info);
            }
        }
        else if (ev.id == "pollution_smog")
        {
            if (choice == 1 && s.budget >= ev.costA)
            {
                s.budget -= ev.costA; s.pollution -= 12f; s.sustainability += 5f;
                CityManager.Instance?.Raise("Industrial filter subsidies cleared smog cloud!", CityManager.AlertLevel.Success);
            }
            else if (choice == 2 && s.budget >= ev.costB)
            {
                s.budget -= ev.costB; s.trafficEfficiency += 8f; s.pollution -= 5f;
                CityManager.Instance?.Raise("Free Bus Day reduced traffic emissions.", CityManager.AlertLevel.Success);
            }
            else
            {
                s.pollution += 4f; s.happiness -= 4f;
                CityManager.Instance?.Raise("Smog advisory issued to citizens.", CityManager.AlertLevel.Warning);
            }
        }

        s.currentEvent = null;
        CityManager.Instance?.RecalculateScore();
        CityManager.Instance?.Notify();
    }
}
