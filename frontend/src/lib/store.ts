import { writable } from "svelte/store";
import { type WorkoutExerciseRead, type ExerciseRead, type WorkoutRead, Api } from "./Api";

export const workouts = writable<WorkoutRead[]>([]);
export const exercises = writable<ExerciseRead[]>([]);
export const workoutExercises = writable<WorkoutExerciseRead[]>([]);