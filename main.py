


if __name__ == "__main__":
    
    # Step 1: Researcher submits research output
    reseracher = Researcher()
    ui = UI()
    controller = SubmissionController()

    data = researcher.submitResearchOutput()
    result = ui.submit(data, controller)

    print(f"\n[Main] Final outcome: {result}")